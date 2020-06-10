from flask import Flask,render_template,request,redirect,url_for,Response

import pandas as pd 
from scrapper import scrap_data

df = pd.DataFrame()




app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrap')
def scrap():
    return render_template('scrap.html')

@app.route('/about')
def about():
    return render_template('comingsoon.html')

@app.route('/contact')
def contact():
    return render_template('comingsoon.html')


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


@app.route('/amazonscrap',methods=('POST','GET'))
def apost():
    global df
    name = 'amazon'
    jsdata = request.get_json()
    num = jsdata['txt']
    df = scrap_data(num,name)
    print(df)


    # return render_template('table.html',tables=[df.to_html(classes='data')], titles=df.columns.values)
    return redirect(url_for('results'))

@app.route('/microsoftscrap',methods=('POST','GET'))
def mpost():
    global df
    name = 'microsoft'
    jsdata = request.get_json()
    num = jsdata['txt']
    df = scrap_data(num,name)
    print(df)


    # return render_template('table.html',tables=[df.to_html(classes='data')], titles=df.columns.values)
    return redirect(url_for('results'))

@app.route('/oraclescrap',methods=('POST','GET'))
def opost():
    global df
    name = 'oracle'
    jsdata = request.get_json()
    num = jsdata['txt']
    df = scrap_data(num,name)
    print(df)


    # return render_template('table.html',tables=[df.to_html(classes='data')], titles=df.columns.values)
    return redirect(url_for('results'))

@app.route('/ibmscrap',methods=('POST','GET'))
def ipost():
    global df
    name = 'ibm'
    jsdata = request.get_json()
    num = jsdata['txt']
    df = scrap_data(num,name)
    print(df)


    # return render_template('table.html',tables=[df.to_html(classes='data')], titles=df.columns.values)
    return redirect(url_for('results'))

@app.route('/results')
def results():  
    return render_template('table.html',tables=[df.to_html(classes='data')], titles=df.columns.values)



@app.route('/download')
def download():
    return Response(
       df.to_csv(),
       mimetype="text/csv",
       headers={"Content-disposition":
       "attachment; filename=filename.csv"})


    


if __name__ == '__main__':
    app.run(debug=True)