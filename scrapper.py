from bs4 import BeautifulSoup
import requests
import pandas as pd 
import time 



#function to scrap_data

def scrap_data(num,name):  

    #create an empty dataframe
    df = pd.DataFrame()


    
    i='https://www.geeksforgeeks.org/tag/' #base url

    
    orig_url= i + name  #store the url in a different variable for reuse
        
    for j in range(1,100):



        #initialize empty lists to hold the attributes of the scrap data

        ID = []
        titles = []
        dates = []
        body = []
        upvotes=[]
        company=[]
        urls = []

        i = orig_url

        if j == 1:
            pass
        else: 
            i=i+"/page/"+str(j)
        try: 
            print(i)
            check = html = requests.get(i)

            #if page is not found break the loop
            if str(check) == "<Response [404]>":
                print("Page {} not found".format(j))
                break
            else:
                pass
            html = html.text

            #create a bs4 object of the html page
            soup = BeautifulSoup(html, "lxml")

            #get all the content with class ='archive-title'
            tag = soup.find(class_='archive-title').span.contents[0]
            print(tag)

            
            articles = soup.find_all('article')
            print(len(articles))

            links = []
            a = articles[0]
            #for each article extract the url
            for article in articles:
                link= article.find('a')['href']
                links.append(link)

            # print(urls)



            



            count = 0


            #loop throughout all the extracted urls and get the content of each post such as text,upvote,title,etc
            for link in links:
                # url = 'https://www.geeksforgeeks.org/amazon-interview-experience-sde-2-3/'


                html = requests.get(link).text
                urls.append(link)

                soup = BeautifulSoup(html, "lxml")



                post = soup.find('div',class_='site-content')

                title = soup.html.head.title.string
                titles.append(title)

                ids = post('article')[0]['id'].split('-')[1]
                ID.append(ids)

                upvote = soup.find('div',class_='plugins upvoteArticle').span.contents
                if upvote[0] == 'Be the First to upvote.':
                    upvote = 0
                    upvotes.append(upvote)
                else:
                    upvotes.append(upvote[0])

                script= soup.find_all('script')[3].contents
                date= script[0].split('\n')[-3].split('=')[1].split('"')[1].split(' ')[0]
                dates.append(date)






                contents = soup.find('div',class_='entry-content')

                #print(contents)


                text = []

                for c in contents.find_all('p'):

                    if c.a:
                        text.append(" ")
                        pass
                    else:

                        #print(c.text)
                        text.append(c.text)
                        
                        
                new_text = []
                for t in text:
                    
                    t = t.replace('\n',' ')
                    new_text.append(t)

                #print(new_text)

                def convert(s): 
                
                    # initialization of string to "" 
                    new = "" 
                
                    # traverse in the string  
                    for x in s: 
                        new += x+' '  
                
                    # return string  
                    return new 


                new_text = convert(new_text)
                body.append(new_text)
                company.append(tag)

                count = count+1
                print(count)
        except Exception as e: 
            print(e)
        try: 

            data = {'ID':ID,'Date':dates,'Titles':titles,'Company':company,'Experience':body,'Upvotes':upvotes,'URLS':urls}
            df = pd.concat([df,pd.DataFrame(data)])

        
            
        


        except Exception as e:
            print(e)

        #if entries in dataframe are more than chosen number break the loop and return the dataframe
        if len(df) >= int(num):
            break
    return df