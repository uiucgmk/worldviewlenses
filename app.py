import os
from flask import Flask
from flask import Flask, request, session, url_for, redirect, render_template, abort, g, flash,json
import pickle
import string
import operator
from operator import itemgetter
from datetime import datetime
import re
import math
import sys
import urlparse
import psycopg2
import json
reload(sys)
sys.setdefaultencoding("utf-8")
# try:
#     from BeautifulSoup import BeautifulSoup
# except ImportError:
#     from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'gmksecret key'

DATABASE_URL = "postgres://tryogbtqiatcdo:a59d49105a9e6af01ff02a9f14ce07152140e1a74925585fde5b8c7a921ccd37@ec2-107-20-191-76.compute-1.amazonaws.com:5432/d7jh292bekuh66"
urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(DATABASE_URL)
#url = urlparse.urlparse(os.environ["DATABASE_URL"])

def run_sql(sql):

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
        #sslmode = 'require'
    )

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    try:
        records = cursor.fetchall()
    except Exception as e:
        records = []
        print 'Exception-----'
        print 'sql: ' + str(sql)
        print 'error: '+ str(e)
    cursor.close()
    return records

@app.route("/",methods=['GET', 'POST'])
def login():

    #sql = "CREATE TABLE Users ( \
    #Id  serial primary key,\
    #Password   VARCHAR(255) not null,);"
    #run_sql(sql)
    if request.method == 'POST':
        username =  request.form['username']
        password =  request.form['password']
        #print username
        #print intertype
        session['username'] = username
        sql= "INSERT INTO users (Username,InterfaceType, Happy, Love, Surprise, Cry,Angry) VALUES ('"+username+"','"+password+"', 0,0,0,0,0);"
        print sql
        run_sql(sql)
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    username = session['username']
    return render_template('index.html')

@app.route('/article1', methods=['GET', 'POST'])
def article1():
    username = session['username']
    dic={}
    f=open("templates/article1/final_out_10155584306476509.txt","r")
    for line in f.readlines():
    	arr=eval(line)
    	print arr[0]
    	if dic.has_key(arr[0]):
    		dic[arr[0]].append(arr[1:])
    	else:
			dic[arr[0]]=[arr[1:]]

    return render_template('article1.html',user=username,dic=dic)

@app.route('/article2', methods=['GET', 'POST'])
def article2():
    username = session['username']
    dic={}
    f=open("templates/article2/final_out_10155792006356509.txt","r")
    for line in f.readlines():
    	arr=eval(line)
    	print arr[0]
    	if dic.has_key(arr[0]):
    		dic[arr[0]].append(arr[1:])
    	else:
			dic[arr[0]]=[arr[1:]]

    return render_template('article2.html',user=username,dic=dic)













if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
