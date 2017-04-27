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

#create table user_info ( Username VARCHAR(255) NOT NULL, Password VARCHAR(255) NOT NULL, Interface VARCHAR(255), Post1 int, Post2 int, Post3 int, Post4 int);
#create table user_info_control ( Username VARCHAR(255) NOT NULL, Password VARCHAR(255) NOT NULL, Interface VARCHAR(255), Post1 int, Post2 int, Post3 int, Post4 int);


	if request.method == 'POST':
		username =  request.form['username']
		password =  request.form['password']
		selection = request.form['selection']
		#print username
		#print intertype
		session['username'] = username
		session['selection'] = selection
		#sql= "INSERT INTO users (Username,Password, Happy, Love, Surprise, Cry,Angry) VALUES ('"+username+"','"+password+"', 0,0,0,0,0);"
		if selection == 'worldviewlenses':
			sql= "INSERT INTO user_info (Username,Password,Interface,Post1, Post2, Post3, Post4 ) VALUES ('"+username+"','"+password+"', 'worldviewlenses',0,0,0,0);"
		elif selection == 'control':
			sql= "INSERT INTO user_info_control (Username,Password,Interface,Post1, Post2, Post3, Post4 ) VALUES ('"+username+"','"+password+"', 'control',0,0,0,0);"

		print sql
		run_sql(sql)
		if selection == 'worldviewlenses':
			return redirect(url_for('index'))
		if selection == 'control':
			return redirect(url_for('cindex'))
	return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
	username = session['username']
	return render_template('index.html')

@app.route('/cindex', methods=['GET', 'POST'])
def cindex():
	username = session['username']
	return render_template('cindex.html')

@app.route('/article1', methods=['GET', 'POST'])
def article1():
	session['post'] = 1
	username = session['username']
	dic={}
	f=open("static/article/NEW_1.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if dic.has_key(arr[0]):
			dic[arr[0]].append(arr[1:])
		else:
			dic[arr[0]]=[arr[1:]]

	#replies
	f_reply=open("static/article/2_replies_to_comment_5550296508_10155584306476509.txt","r")
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

	return render_template('article1.html',user=username,dic=dic,replydic=dic2)

@app.route('/article2', methods=['GET', 'POST'])
def article2():
	username = session['username']
	session['post'] = 2
	dic={}
	f=open("static/article/NEW_2.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if dic.has_key(arr[0]):
			dic[arr[0]].append(arr[1:])
		else:
			dic[arr[0]]=[arr[1:]]

	#replies
	f_reply=open("static/article/2_replies_to_comment_5550296508_10155792006356509.txt","r")
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



	return render_template('article2.html',user=username,dic=dic,replydic=dic2)

@app.route('/article3', methods=['GET', 'POST'])
def article3():
	username = session['username']
	session['post'] = 3
	dic={}
	f=open("static/article/NEW_3.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if dic.has_key(arr[0]):
			dic[arr[0]].append(arr[1:])
		else:
			dic[arr[0]]=[arr[1:]]

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


	return render_template('article3.html',user=username,dic=dic,replydic=dic2)

@app.route('/article4', methods=['GET', 'POST'])
def article4():
	username = session['username']
	session['post'] = 4
	dic={}
	f=open("static/article/NEW_4.txt","r")
	for line in f.readlines():
		arr=eval(line)
		#print arr[0]
		if dic.has_key(arr[0]):
			dic[arr[0]].append(arr[1:])
		else:
			dic[arr[0]]=[arr[1:]]

	#replies
	f_reply=open("static/article/2_replies_to_comment_5550296508_10155699096601509.txt","r")
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


	return render_template('article4.html',user=username,dic=dic,replydic=dic2)

@app.route('/carticle1', methods=['GET', 'POST'])
def carticle1():
	session['post'] = 1
	username = session['username']
	# dic = pickle.load(open( "./static/article/article1.p", "rb" ))
	# print dic
	# return render_template('carticle1.html',user=username,dic=dic)

	dic={}
	f=open("static/article/NEW_final_out_10155584306476509.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if not dic.has_key(arr[3]):
			dic[arr[3]]=[arr[2],arr[1],arr[0]]
		else:
			dic[arr[3]].append(arr[0])

	#replies
	f_reply=open("static/article/2_replies_to_comment_5550296508_10155584306476509.txt","r")
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

	return render_template('carticle1.html',user=username,dic=dic,replydic=dic2)



@app.route('/carticle2', methods=['GET', 'POST'])
def carticle2():
	session['post'] = 2
	username = session['username']
	dic={}
	f=open("static/article/NEW_final_out_10155792006356509.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if not dic.has_key(arr[3]):
			dic[arr[3]]=[arr[2],arr[1],arr[0]]
		else:
			dic[arr[3]].append(arr[0])

	#replies
	f_reply=open("static/article/2_replies_to_comment_5550296508_10155792006356509.txt","r")
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

	return render_template('carticle2.html',user=username,dic=dic,replydic=dic2)

@app.route('/carticle3', methods=['GET', 'POST'])
def carticle3():
	session['post'] = 3
	username = session['username']
	dic={}
	f=open("static/article/NEW_final_out_10155749891186509.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if not dic.has_key(arr[3]):
			dic[arr[3]]=[arr[2],arr[1],arr[0]]
		else:
			dic[arr[3]].append(arr[0])

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

	return render_template('carticle3.html',user=username,dic=dic,replydic=dic2)

@app.route('/carticle4', methods=['GET', 'POST'])
def carticle4():
	session['post'] = 4
	username = session['username']
	dic={}
	f=open("static/article/NEW_final_out_10155699096601509.txt","r")
	for line in f.readlines():
		arr=eval(line)
		if not dic.has_key(arr[3]):
			dic[arr[3]]=[arr[2],arr[1],arr[0]]
		else:
			dic[arr[3]].append(arr[0])

	#replies
	f_reply=open("static/article/2_replies_to_comment_5550296508_10155699096601509.txt","r")
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

	return render_template('carticle4.html',user=username,dic=dic,replydic=dic2)






# @app.route('/carticle2', methods=['GET', 'POST'])
# def carticle2():
# 	session['post'] = 2
# 	username = session['username']
# 	dic = pickle.load(open( "./static/article/article4.p", "rb" ))
# 	print dic
# 	return render_template('carticle2.html',user=username,dic=dic)

# @app.route('/carticle3', methods=['GET', 'POST'])
# def carticle3():
# 	session['post'] = 3
# 	username = session['username']
# 	dic = pickle.load(open( "./static/article/article3.p", "rb" ))
# 	print dic
# 	return render_template('carticle3.html',user=username,dic=dic)

# @app.route('/carticle4', methods=['GET', 'POST'])
# def carticle4():
# 	session['post'] = 4
# 	username = session['username']
# 	dic = pickle.load(open( "./static/article/article2.p", "rb" ))
# 	print dic
# 	return render_template('carticle4.html',user=username,dic=dic)

@app.route('/share', methods=['GET', 'POST'])
def share():
	#create table share (Username VARCHAR(255) NOT NULL, Post int,Sentiment VARCHAR(255),Aspect VARCHAR(255),Comment TEXT,Whowhy TEXT);
	#create table share_control2 (Username VARCHAR(255) NOT NULL, Post int,Sentiment VARCHAR(255),Aspect VARCHAR(255),Comment TEXT,Whowhy TEXT);

	post=session['post']
	username = session['username']
	selection = session['selection']
	if request.method == 'POST':
		user_data = request.form.getlist('shareid[]')
		print user_data
		whowhy_data = request.form['whowhy']
		if selection == 'worldviewlenses':
			sql= "INSERT INTO share (Username,Post,Sentiment,Aspect,Comment,whowhy) VALUES ('"+username+"','"+str(post)+"','"+user_data[1]+"','"+user_data[0]+"','"+user_data[2].replace("'","")+"','"+whowhy_data+"');"
		elif selection == 'control':
		#	sql= "INSERT INTO share_control (Username,Post,Sentiment,Comment,whowhy) VALUES ('"+username+"','"+str(post)+"','"+user_data[0]+"','"+user_data[1].replace("'","")+"','"+whowhy_data+"');"
			sql= "INSERT INTO share_control2 (Username,Post,Sentiment,Aspect,Comment,whowhy) VALUES ('"+username+"','"+str(post)+"','"+user_data[1]+"','"+user_data[0]+"','"+user_data[2].replace("'","")+"','"+whowhy_data+"');"

		run_sql(sql)
		return 'OK'

@app.route('/checkeditems', methods=['GET', 'POST'])
def checkeditems():
	#create table checkeditems ( Username VARCHAR(255),Post int,Sentiment VARCHAR(255),Aspect VARCHAR(255),Comment TEXT );
	if request.method == 'POST':
		post=session['post']
		all_data=[]
		all_data_raw=[]
		reaction_data=[]
		username = session['username']
		all_data_raw = request.form.getlist('all_data[]')
		reaction_data = request.form.getlist('reaction_data[]')
		#for checked items
		for i in range(0,len(all_data_raw)):
			all_data=all_data_raw[i].split("\t\t")
			sql= "INSERT INTO checkeditems (Username,Post,Sentiment,Aspect,Comment) VALUES ('"+username+"','"+str(post)+"','"+all_data[0]+"','"+all_data[1]+"','"+all_data[2]+"');"
			#print sql
			run_sql(sql)


		#for reaction data
		#create table reactions ( Username VARCHAR(255) NOT NULL, Post int, Like_reaction int, Love int, Haha int, Surprise int, Sad int, Anger int, Neutral int);
		sql= "INSERT INTO reactions (Username,Post, Like_reaction, Love, Haha, Surprise, Sad, Anger,Neutral ) VALUES ('"+username+"','"+str(post)+"','"+str(reaction_data[0].split(":")[1])+"','"+str(reaction_data[1].split(":")[1])+"','"+str(reaction_data[2].split(":")[1])+"','"+str(reaction_data[3].split(":")[1])+"','"+str(reaction_data[4].split(":")[1])+"','"+str(reaction_data[5].split(":")[1])+"','"+str(reaction_data[6].split(":")[1])+"');"
		#print sql
		run_sql(sql)

		#update the worked post 0-->1
		sql= "UPDATE user_info SET Post"+str(post)+"= 1 WHERE Username='"+username+"';"
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
		if selection == 'worldviewlenses':
			sql= "INSERT INTO postcomment (Username,Post,Comment) VALUES ('"+username+"','"+str(post)+"','"+comment_data+"');"
		elif selection == 'control':
			sql= "INSERT INTO postcomment_control (Username,Post,Comment) VALUES ('"+username+"','"+str(post)+"','"+comment_data+"');"
		run_sql(sql)
		return 'OK'

@app.route('/checkeditems_control', methods=['GET', 'POST'])
def checkeditems_control():
	#create table checkeditems ( Username VARCHAR(255),Post int,Sentiment VARCHAR(255),Aspect VARCHAR(255),Comment TEXT );
	if request.method == 'POST':
		post=session['post']
		all_data=[]
		all_data_raw=[]
		reaction_data=[]
		username = session['username']
		all_data_raw = request.form.getlist('all_data[]')
		reaction_data = request.form.getlist('reaction_data[]')
		#for checked items
		for i in range(0,len(all_data_raw)):
			all_data=all_data_raw[i].split("\t\t")
			sql= "INSERT INTO checkeditems_control (Username,Post,Sentiment,Comment) VALUES ('"+username+"','"+str(post)+"','"+all_data[0]+"','"+all_data[1].replace("'","")+"');"
			print sql
			run_sql(sql)


		#for reaction data
		#create table reactions ( Username VARCHAR(255) NOT NULL, Post int, Like_reaction int, Love int, Haha int, Surprise int, Sad int, Anger int, Neutral int);
		sql= "INSERT INTO reactions_control (Username,Post, Like_reaction, Love, Haha, Surprise, Sad, Anger,Neutral ) VALUES ('"+username+"','"+str(post)+"','"+str(reaction_data[0].split(":")[1])+"','"+str(reaction_data[1].split(":")[1])+"','"+str(reaction_data[2].split(":")[1])+"','"+str(reaction_data[3].split(":")[1])+"','"+str(reaction_data[4].split(":")[1])+"','"+str(reaction_data[5].split(":")[1])+"','"+str(reaction_data[6].split(":")[1])+"');"
		#print sql
		run_sql(sql)

		#update the worked post 0-->1
		sql= "UPDATE user_info_control SET Post"+str(post)+"= 1 WHERE Username='"+username+"';"
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
		if selection == 'worldviewlenses':
			sql= "INSERT INTO reply_comment (Username,Post,Aspect,Sentiment,Comment,Reply) VALUES ('"+username+"','"+str(post)+"','"+all_data[0][5:]+"','"+all_data[1]+"','"+all_data[2].replace("'","")+"','"+reply_data.replace("'","")+"');"
			print sql
		elif selection == 'control':
			sql= "INSERT INTO reply_comment_control (Username,Post,Aspect,Sentiment,Comment,Reply) VALUES ('"+username+"','"+str(post)+"','"+all_data[0][5:]+"','"+all_data[1]+"','"+all_data[2].replace("'","")+"','"+reply_data.replace("'","")+"');"
		else:
			print "error occurred in /replycomment"

		run_sql(sql)
	return 'OK'


if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port,debug=True)
