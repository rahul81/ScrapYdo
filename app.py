from flask import Flask,render_template,request,redirect,url_for,Response

import pandas as pd 
from scrapper import scrap_data


#create an empty pandas datframe
df = pd.DataFrame()



#create the flask app
app = Flask(__name__)


#define the endpoints of the app


#home page
@app.route('/')
def index():
    return render_template('index.html')


#scrapper page
@app.route('/scrap')
def scrap():
    return render_template('scrap.html')


#about page
@app.route('/about')
def about():
    return render_template('comingsoon.html')


##contact page
@app.route('/contact')
def contact():
    return render_template('comingsoon.html')


#scraping page for each company

@app.route('/amazon')
def amazon():
    return render_template('amazon.html')

@app.route('/microsoft')
def microsoft():
    return render_template('microsoft.html')

@app.route('/ibm')
def ibm():
    return render_template('ibm.html')


@app.route('/oracle')
def oracle():
    return render_template('oracle.html')



#post request endpoint for recieving the chosen number from user and start scraping

@app.route('/amazonscrap',methods=('POST','GET'))
def apost():
    global df
    name = 'amazon'
    jsdata = request.get_json()
    num = jsdata['txt']
    df = scrap_data(num,name)
    print(df)


    return redirect(url_for('results'))

@app.route('/microsoftscrap',methods=('POST','GET'))
def mpost():
    global df
    name = 'microsoft'
    jsdata = request.get_json()
    num = jsdata['txt']
    df = scrap_data(num,name)
    print(df)


    return redirect(url_for('results'))

@app.route('/oraclescrap',methods=('POST','GET'))
def opost():
    global df
    name = 'oracle'
    jsdata = request.get_json()
    num = jsdata['txt']
    df = scrap_data(num,name)
    print(df)


    return redirect(url_for('results'))

@app.route('/ibmscrap',methods=('POST','GET'))
def ipost():
    global df
    name = 'ibm'
    jsdata = request.get_json()
    num = jsdata['txt']
    df = scrap_data(num,name)
    print(df)


    return redirect(url_for('results'))


#endpoint for the results page

@app.route('/results')
def results():  
    return render_template('table.html',tables=[df.to_html(classes='data')], titles=df.columns.values)



#return a csv file of all the scrapped interviews
@app.route('/download')
def download():
    return Response(
       df.to_csv(),
       mimetype="text/csv",
       headers={"Content-disposition":
       "attachment; filename=filename.csv"})


    

#initialize the webapp
if __name__ == '__main__':
    app.run(debug=True)