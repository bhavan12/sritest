from io import BytesIO
import numpy as np
import pandas as pd
import psycopg2
from flask import Flask, render_template,request,send_file, make_response,json
from flask_bootstrap import Bootstrap
from pandas.io.json import json_normalize
from flask_cors import  CORS,cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
Bootstrap(app)
import xgboost as xgb
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
con = psycopg2.connect("dbname=dfhaphi9vtlee6 user=qcmezkrwpidutn password=3fd32869bc0d2fb997e2c47dfe339f552267e7c40bc00949638ae3b43947a64d host=ec2-107-20-183-142.compute-1.amazonaws.com")
@app.route('/app1',methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def index():
  if request.method == 'GET':
    '''userDetails = request.form
    num1= userDetails['num1']
    num2 = userDetails['num2']
    num3 = userDetails['num3']
    num1 = int(num1)
    num2 = int(num2)
      num3 = int(num3)'''
    num1 = request.args.get('lid')
    num2 = request.args.get('mid')
    num3 = request.args.get('nid')
    sql = """select * from qms.aud2"""
    df = pd.io.sql.read_sql(sql, con)
    DepartmentID = df['deptid']
    AuditorID = df['auditorid']
    SiteID = df['siteid']
    cper = df['cper']
    X = np.array([AuditorID, SiteID, DepartmentID]).T
    y = np.array(cper)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.0)
    abc = AdaBoostRegressor(n_estimators=50,
                            learning_rate=1)
    model = abc.fit(X_train, y_train)
    z = np.array([num1,num2,num3]).reshape(1, -1)
    # Predict the response for test dataset
    y_pred = model.predict(z)
    y_pred=int(y_pred)
    pythonDictionary = {'a':num1, 'b':num2, 'c':num3,'e':y_pred}
    return  json.dumps(pythonDictionary)
   # return render_template('index.html',a=num1,b=num2,c=num3,e=y_pred)
  '''else: 
    sql = """select * from qms.aud2""" 
    df = pd.io.sql.read_sql(sql, con)
    DepartmentID = df['deptid']
    AuditorID = df['auditorid']
    SiteID = df['siteid']
    noofobser = df['noofaber']
    cper = df['cper']
    X = np.array([AuditorID, SiteID, DepartmentID]).T
    y = np.array(cper)
    # Split dataset into training set and test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)  # 70% training and 30% test

    # Create adaboost classifer object
    abc = AdaBoostRegressor(n_estimators=50,
                            learning_rate=1)
    # Train Adaboost Classifer
    model = abc.fit(X_train, y_train)
    # Predict the response for test dataset
    y_pred = model.predict(X_test)
    a=np.sqrt(mean_squared_error(y_test, y_pred))
    x = np.array(AuditorID)
    #x = np.append(x, num1)
    x1 = np.array(SiteID)
    #x1 = np.append(x, num2)
    x2 = np.array(DepartmentID)
    #x2 = np.append(x, num3)
    x3 = np.array(noofobser)
    #x3 = np.append(x, num4)
    y1 = np.array(cper)
    y2 = np.append(y, y_pred)
    z = zip(x, x1, x2, y)
    return render_template('index.html', z=z,a=a)

@app.route('/delete')
def user():
    print("")'''
    

