from io import BytesIO
import numpy as np
import pandas as pd
import psycopg2
from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
import xgboost as xgb
con = psycopg2.connect("dbname=dfhaphi9vtlee6 user=qcmezkrwpidutn password=3fd32869bc0d2fb997e2c47dfe339f552267e7c40bc00949638ae3b43947a64d host=ec2-107-20-183-142.compute-1.amazonaws.com")
@app.route('/',methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    userDetails = request.form
    num1= userDetails['num1']
    num2 = userDetails['num2']
    num3 = userDetails['num3']
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    sql = """select * from qms.aud2"""
    df = pd.io.sql.read_sql(sql, con)
    DepartmentID = df['deptid']
    AuditorID = df['auditorid']
    SiteID = df['siteid']
    cper = df['cper']
    X = np.array([AuditorID, SiteID, DepartmentID]).T
    y = np.array(cper)
    from sklearn.model_selection import train_test_split
    x1 = np.array(AuditorID)
    x2 = np.array(DepartmentID)
    z = zip(x1, x2)
    return render_template('index.html', z=z)
