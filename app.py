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
from collections import OrderedDict
import random
import time
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.secret_key = 'gmksecret key'

DATABASE_URL = "postgres://tryogbtqiatcdo:a59d49105a9e6af01ff02a9f14ce07152140e1a74925585fde5b8c7a921ccd37@ec2-107-20-191-76.compute-1.amazonaws.com:5432/d7jh292bekuh66"
urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(DATABASE_URL)

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
	# records=[]
	# try:
	# 	records = cursor.fetchall()
	# except Exception as e:
	# 	print 'Exception-----'
	# 	pass
	cursor.close()
	return
	# return records


@app.route("/",methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		username =  request.form['username']
		# password =  request.form['password']
		selection = request.form['selection']

		session['username'] = username
		session['selection'] = selection #selection is A,B,C,D 
			
		sql= "INSERT INTO new_user (Username,Interface,Post3, Post5 ) VALUES ('"+username+"','"+selection+"' ,0,0);"

		print sql
		run_sql(sql)
		if selection:
			return redirect(url_for('index'))

	return render_template('login.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
	username = session['username']
	return render_template('index.html', interface=session['selection'])


@app.route('/nocnn3', methods=['GET', 'POST'])
def nocnn3():
	return render_template('nocnn3.html')

@app.route('/nocnn5', methods=['GET', 'POST'])
def nocnn5():
	return render_template('nocnn5.html')


@app.route('/A_article3', methods=['GET', 'POST'])
def aarticle3():
	session['post'] = 3
	username = session['username']

	dic={}
	#fw3=open("static/article/BALANCED_C_3.txt","w")
	f=open("static/article/BALANCED_3.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if not dic.has_key(arr[3]):
			dic[arr[3]]=[arr[2],arr[1],arr[0]]
			#fw3.write(str([arr[2],arr[1],arr[0],arr[3]])+"\n")
	#fw3.close()

	#randomize
	random.seed(time.clock())
	keys =  list(dic.keys())
	random.shuffle(keys)
	randomdic=OrderedDict()
	for key in keys:
		randomdic[key]=dic[key] 

	f_reply=open("static/article/2_replies_to_comment_5550296508_10155749891186509.txt","r")
	arr=[]
	dic2={}
	for line in f_reply.readlines():
		arr=eval(line)
		arr[5]=arr[5].replace("'","")
		arr[5]=arr[5].replace('"','')

		if dic2.has_key(arr[0]):
			dic2[arr[0]].append(arr[5])
		else:
			dic2[arr[0]]=[arr[5]]

	#return render_template('carticle3.html',user=username,dic=dic,replydic=dic2)
	#####FOR AMT: later replace the upper one 
	#return render_template('carticle3.html',user=username,dic=randomdic,replydic=dic2)
	return render_template('carticle3.html',user=username,dic=randomdic,replydic=dic2)


@app.route('/A_article5', methods=['GET', 'POST'])
def aarticle5():
	session['post'] = 5
	username = session['username']
	dic={}
	#fw5=open("static/article/BALANCED_C_5.txt","w")
	f=open("static/article/BALANCED_5.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if not dic.has_key(arr[3]):
			dic[arr[3]]=[arr[2],arr[1],arr[0]]
			#fw5.write(str([arr[2],arr[1],arr[0],arr[3]])+"\n")
	#fw5.close()
	random.seed(time.clock())
	keys =  list(dic.keys())
	random.shuffle(keys)
	randomdic=OrderedDict()
	for key in keys:
		randomdic[key]=dic[key] 
	
	#replies
	f_reply=open("static/article/2_replies_to_comment_15704546335_10155095856676336.txt","r")
	arr=[]
	dic2={}
	for line in f_reply.readlines():
		arr=eval(line)
		arr[5]=arr[5].replace("'","")
		arr[5]=arr[5].replace('"','')

		if dic2.has_key(arr[0]):
			dic2[arr[0]].append(arr[5])
		else:
			dic2[arr[0]]=[arr[5]]

	#####FOR AMT: later replace the upper one 
	#return render_template('carticle5.html',user=username,dic=randomdic,replydic=dic2)
	return render_template('carticle5.html',user=username,dic=randomdic,replydic=dic2)


@app.route('/B_article3', methods=['GET', 'POST'])
def barticle3():

	username = session['username']
	session['post'] = 3
	dic={}
	f=open("static/article/BALANCED_3.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if not dic.has_key(arr[3]):
			dic[arr[3]]=[arr[2],arr[1],arr[0]] #key=id, comment[0], sentiment[1]. keyword[2]
	
	
	#randomize
	random.seed(time.clock())
	randint=random.randint(0,1) #0 or 1
	if randint==0:
		sent=["negative","positive"]
	else:
		sent=["positive","negative"]
	keys =  list(dic.keys())
	random.shuffle(keys)
	randomdic=OrderedDict()
	for key in keys:
		randomdic[key]=dic[key]
	
		
	#replies
	f_reply=open("static/article/2_replies_to_comment_5550296508_10155749891186509.txt","r")
	arr=[]
	dic2={}
	for line in f_reply.readlines():
		arr=eval(line)
		arr[5]=arr[5].replace("'","")
		arr[5]=arr[5].replace('"','')

		if dic2.has_key(arr[0]):
			dic2[arr[0]].append(arr[5])
		else:
			dic2[arr[0]]=[arr[5]]

	return render_template('B_article3.html',user=username,dic=randomdic,replydic=dic2,sentiment=sent)

@app.route('/B_article5', methods=['GET', 'POST'])
def barticle5():
	username = session['username']
	session['post'] = 5
	dic={}
	f=open("static/article/BALANCED_5.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if not dic.has_key(arr[3]):
			dic[arr[3]]=[arr[2],arr[1],arr[0]]
	
	random.seed(time.clock())
	randint=random.randint(0,1) #0 or 1
	if randint==0:
		sent=["negative","positive"]
	else:
		sent=["positive","negative"]
	keys =  list(dic.keys())
	random.shuffle(keys)
	randomdic=OrderedDict()
	for key in keys:
		randomdic[key]=dic[key]

	f_reply=open("static/article/2_replies_to_comment_15704546335_10155095856676336.txt","r")
	arr=[]
	dic2={}
	for line in f_reply.readlines():
		arr=eval(line)
		arr[5]=arr[5].replace("'","")
		arr[5]=arr[5].replace('"','')

		if dic2.has_key(arr[0]):
			dic2[arr[0]].append(arr[5])
		else:
			dic2[arr[0]]=[arr[5]]

	return render_template('B_article5.html',user=username,dic=randomdic,replydic=dic2, sentiment=sent)

@app.route('/C_article3', methods=['GET', 'POST'])
def carticle3():

	username = session['username']
	session['post'] = 3
	dic={}
	f=open("static/article/BALANCED_3.txt","r") #[0]key [1]sent [2]comment [3]id
	for line in f.readlines():
		arr=eval(line)
		if dic.has_key(arr[0]):
			dic[arr[0]].append(arr[1:])
		else:
			dic[arr[0]]=[arr[1:]]
	
	#randomize
	random.seed(time.clock())
	keywords =  list(dic.keys())
	random.shuffle(keywords)
	randomdic=OrderedDict()
	for keyword in keywords:
		#randomize the aspect
		randomdic[keyword]=dic[keyword]
		#randomize the comments within one aspect
		random.shuffle(randomdic[keyword])




	f_reply=open("static/article/2_replies_to_comment_5550296508_10155749891186509.txt","r")
	arr=[]
	dic2={}
	for line in f_reply.readlines():
		arr=eval(line)
		arr[5]=arr[5].replace("'","")
		arr[5]=arr[5].replace('"','')

		if dic2.has_key(arr[0]):
			dic2[arr[0]].append(arr[5])
		else:
			dic2[arr[0]]=[arr[5]]

	return render_template('C_article3.html',user=username,dic=randomdic,replydic=dic2)


@app.route('/C_article5', methods=['GET', 'POST'])
def carticle5():
	username = session['username']
	session['post'] = 5
	dic={}
	f=open("static/article/BALANCED_5.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if dic.has_key(arr[0]):
			dic[arr[0]].append(arr[1:])
		else:
			dic[arr[0]]=[arr[1:]]


	#randomize
	random.seed(time.clock())
	keywords =  list(dic.keys())
	random.shuffle(keywords)
	randomdic=OrderedDict()
	for keyword in keywords:
		#randomize the aspect
		randomdic[keyword]=dic[keyword]
		#randomize the comments within one aspect
		random.shuffle(randomdic[keyword])

	#replies
	f_reply=open("static/article/2_replies_to_comment_15704546335_10155095856676336.txt","r")
	arr=[]
	dic2={}
	for line in f_reply.readlines():
		arr=eval(line)
		arr[5]=arr[5].replace("'","")
		arr[5]=arr[5].replace('"','')

		if dic2.has_key(arr[0]):
			dic2[arr[0]].append(arr[5])
		else:
			dic2[arr[0]]=[arr[5]]

	return render_template('C_article5.html',user=username,dic=randomdic,replydic=dic2)


@app.route('/D_article3', methods=['GET', 'POST'])
def darticle3():
	username = session['username']
	session['post'] = 3
	dic={}
	f=open("static/article/BALANCED_3.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if dic.has_key(arr[0]):
			dic[arr[0]].append(arr[1:])
		else:
			dic[arr[0]]=[arr[1:]]

	#randomize
	random.seed(time.clock())
	randint=random.randint(0,1) #0 or 1
	if randint==0:
		sent=["negative","positive"]
	else:
		sent=["positive","negative"]
	keywords =  list(dic.keys())
	random.shuffle(keywords)
	randomdic=OrderedDict()
	for keyword in keywords:
		#randomize the aspect
		randomdic[keyword]=dic[keyword]
		#randomize the comments within one aspect
		random.shuffle(randomdic[keyword])


	f_reply=open("static/article/2_replies_to_comment_5550296508_10155749891186509.txt","r")
	arr=[]
	dic2={}
	for line in f_reply.readlines():
		arr=eval(line)
		arr[5]=arr[5].replace("'","")
		arr[5]=arr[5].replace('"','')

		if dic2.has_key(arr[0]):
			dic2[arr[0]].append(arr[5])
		else:
			dic2[arr[0]]=[arr[5]]

	return render_template('article3.html',user=username,dic=randomdic,replydic=dic2,sentiment=sent)


@app.route('/D_article5', methods=['GET', 'POST'])
def darticle5():
	username = session['username']
	session['post'] = 5
	dic={}
	f=open("static/article/BALANCED_5.txt","r")
	for line in f.readlines():
		arr=eval(line)
		#print arr[0]
		if dic.has_key(arr[0]):
			dic[arr[0]].append(arr[1:])
		else:
			dic[arr[0]]=[arr[1:]]

	#randomize
	random.seed(time.clock())
	randint=random.randint(0,1) #0 or 1
	if randint==0:
		sent=["negative","positive"]
	else:
		sent=["positive","negative"]
	keywords =  list(dic.keys())
	random.shuffle(keywords)
	randomdic=OrderedDict()
	for keyword in keywords:
		#randomize the aspect
		randomdic[keyword]=dic[keyword]
		#randomize the comments within one aspect
		random.shuffle(randomdic[keyword])

	#replies
	f_reply=open("static/article/2_replies_to_comment_15704546335_10155095856676336.txt","r")
	arr=[]
	dic2={}
	for line in f_reply.readlines():
		arr=eval(line)
		arr[5]=arr[5].replace("'","")
		arr[5]=arr[5].replace('"','')

		if dic2.has_key(arr[0]):
			dic2[arr[0]].append(arr[5])
		else:
			dic2[arr[0]]=[arr[5]]

	#####FOR AMT: later replace the upper one 
	#return render_template('article5.html',user=username,dic=dic,replydic=dic2)
	return render_template('article5.html',user=username,dic=randomdic,replydic=dic2,sentiment=sent)



@app.route('/share', methods=['GET', 'POST'])
def share():
	#create table share (Username VARCHAR(255) NOT NULL, Post int,Sentiment VARCHAR(255),Aspect VARCHAR(255),Comment TEXT,Whowhy TEXT);
	#create table share_control2 (Username VARCHAR(255) NOT NULL, Post int,Sentiment VARCHAR(255),Aspect VARCHAR(255),Comment TEXT,Whowhy TEXT);

	post=session['post']
	username = session['username']
	selection = session['selection']
	if request.method == 'POST':
		user_data = request.form.getlist('shareid[]')
		whowhy_data = request.form['whowhy']
		print user_data
		sql= "INSERT INTO new_share (Username,Post,Sentiment,Aspect,Comment,Why) VALUES ('"+username+"','"+str(post)+"','"+user_data[0]+"','"+user_data[1]+"','"+user_data[2]+"','"+whowhy_data+"');"
		
		run_sql(sql)
		return 'OK'

@app.route('/checkeditems', methods=['GET', 'POST'])
def checkeditems():
	#create table checkeditems ( Username VARCHAR(255),Post int,Sentiment VARCHAR(255),Aspect VARCHAR(255),Comment TEXT );
	if request.method == 'POST':
		post=session['post']
		reaction_data=[]
		username = session['username']
		reaction_data = request.form.getlist('reaction_data[]')
		

		#for reaction data
		#create table reactions ( Username VARCHAR(255) NOT NULL, Post int, Like_reaction int, Love int, Haha int, Surprise int, Sad int, Anger int, Neutral int);
		sql= "INSERT INTO new_reactions (Username,Post, Like_reaction, Love, Haha, Surprise, Sad, Anger,Neutral ) VALUES ('"+username+"','"+str(post)+"','"+str(reaction_data[0].split(":")[1])+"','"+str(reaction_data[1].split(":")[1])+"','"+str(reaction_data[2].split(":")[1])+"','"+str(reaction_data[3].split(":")[1])+"','"+str(reaction_data[4].split(":")[1])+"','"+str(reaction_data[5].split(":")[1])+"','"+str(reaction_data[6].split(":")[1])+"');"
		#print sql
		run_sql(sql)

		#update the worked post 0-->1
		sql= "UPDATE new_user SET Post"+str(post)+"= 1 WHERE Username='"+username+"';"
		run_sql(sql)

		return 'OK'
		


@app.route('/postcomment', methods=['GET', 'POST'])
def postcomment():
	#create table postcomment (Username VARCHAR(255) NOT NULL, Post int, Comment TEXT);
	post=session['post']
	username = session['username']
	selection = session['selection']
	if request.method == 'POST':
		comment_data = request.form['post_comment']
		sql= "INSERT INTO new_postcomment (Username,Post,Comment) VALUES ('"+username+"','"+str(post)+"','"+comment_data+"');"
		run_sql(sql)
		return 'OK'



@app.route('/replycomment', methods=['GET', 'POST'])
def replycomment():
	#create table reply_comment_control ( Username VARCHAR(255),Post int,Aspect VARCHAR(255),Sentiment VARCHAR(255),Comment TEXT,Reply TEXT );
	#create table reply_comment ( Username VARCHAR(255),Post int,Aspect VARCHAR(255),Sentiment VARCHAR(255),Comment TEXT,Reply TEXT );
	if request.method == 'POST':
		post=session['post']
		username = session['username']
		selection=session['selection']

		all_data=[]
		all_data= request.form.getlist('all_data[]')
		reply_data = request.form['reply_data']
		print reply_data
		sql= "INSERT INTO new_reply_comment (Username,Post,Sentiment,Aspect,Comment,Reply) VALUES ('"+username+"','"+str(post)+"','"+all_data[0][5:]+"','"+all_data[1]+"','"+all_data[2]+"','"+reply_data.replace("'","")+"');"
		
		run_sql(sql)
	return 'OK'

@app.route('/readmore', methods=['GET', 'POST'])
def readmore():
	if request.method == 'POST':
		post=session['post']
		username = session['username']
		selection=session['selection']
		read_data= request.form.get('read_data')
		all_data=read_data.split("\t\t")
		
		sql= "INSERT INTO new_readmore (Username,Post,Sentiment,Aspect,Comment) VALUES ('"+username+"','"+str(post)+"','"+all_data[0]+"','"+all_data[1]+"','"+all_data[2]+"');"
		#print sql
		run_sql(sql)

		print read_data
	return 'OK'


if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port,debug=True)
