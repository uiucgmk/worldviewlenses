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
reload(sys)
sys.setdefaultencoding("utf-8")
# try:
#     from BeautifulSoup import BeautifulSoup
# except ImportError:
#     from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'gmksecret key'

@app.route("/")
def test():
    return render_template('article.html')

@app.route("/hello")
def hello():
    #return render_template('newuser.html', error=None)
    return index_dict_desc.keys()[0]

@app.route('/web', methods=['GET', 'POST'])
def web():

    if request.method == 'POST':

        isfinish = request.form['finish']

        input_update_list = request.form['inputupdate']
        #print "Update"
        #print input_update_list
        update_list = request.form['update']
        print "Update"
        print update_list

        testid = request.form['testid']
        pagecount = int(request.form['pagecount'])
        #### Comment Out for Experiment
        leng = int(request.form['leng'])

        weblist = []
        for i in xrange(leng):
            key = 'u'+str(i)
            web = request.form[key]
            weblist.append(web)

        selectedlist = []
        for i in xrange(leng):

            key = 's'+str(i)

            selval = request.form[key]

            if selval == 'yes':
                selectedlist.append(i)

        selectedwebs = [weblist[i] for i in selectedlist]

        if isfinish == "yes":

            history = pickle.load(open( "./resources/"+testid+".p", "rb" ))
            history[testid].append(("Final","",weblist,"",str(datetime.now())))
            f = open("./resources/"+testid+".txt",'w')

            for (x,y,z,w,t) in history[testid]:
                f.write('Step:' + str(x)+'\n')
                f.write('Query:' + y+'\n')
                f.write('Select Page:' + '\t'.join(z)+ '\n')
                f.write('Select Keys:' + w+ '\n')
                f.write('Time:' + t+ '\n')

            pickle.dump(history, open( "./resources/"+testid+".p", "wb" ) )

            return redirect(url_for('first'))



        else:

            history = pickle.load(open( "./resources/"+testid+".p", "rb" ))
            history[testid].append((pagecount,input_update_list,selectedwebs,update_list,str(datetime.now())))
            pickle.dump(history, open( "./resources/"+testid+".p", "wb" ) )
            pagecount += 1
            (t_feature,t_detail_feature,d_feature) = build_updated_feature_vector_interactive(input_update_list,update_list, selectedwebs)
            result = compute_similarity(feature_space,t_feature+t_detail_feature + d_feature)
            web_results = return_search_result(result,feature_space)

            print "After Update"
            print update_list
            return render_template('web.html',weblist =  web_results,length = len(web_results),pagecount = pagecount, testid = testid, oldquery = input_update_list,oldupdatesedits = update_list )
###### End Comment Here
        #return redirect(url_for('hello'))
    elif request.method == 'GET':
        print "I am in GET"
        testid = session['testid']
        pagecount = session['pagecount']
        web_results = pickle.load(open( "./resources/info.p", "rb" ))
        history = pickle.load(open( "./resources/"+testid+".p", "rb" ))
        (oldpagecount,oldquery,oldweblist,oldupdate_edits,oldtime) = history[testid][-1]
        #print "HAHAH"
        #print (oldpagecount,oldquery,oldweblist,oldupdate_edits)

        return render_template('web.html',weblist =  web_results,length = len(web_results),pagecount = pagecount, testid = testid, oldquery = oldquery, oldupdateedits = oldupdate_edits )

@app.route('/', methods=['GET', 'POST'])
def first():
    history = {}
    if request.method == 'POST':
        testid =  request.form['testid']
        session['testid'] = testid
        session['pagecount'] = 0
        select =  request.form['retrievalmethod']
        history[testid] = []
        pickle.dump(history, open( "./resources/"+testid+".p", "wb" ) )
        if select == 'interactive':
            return redirect(url_for('query'))
        elif select == 'regular':
            return redirect(url_for('regular_query'))

    return render_template('first.html')


@app.route('/query', methods=['GET', 'POST'])
def query():

    if request.method == 'POST':
        query =  request.form['query']
        print "Query: " + query
        wordlist = load_file_tokens(query)
        (t_feature,t_detail_feature,d_feature) = build_initial_feature(wordlist)
        result = compute_similarity(feature_space,t_feature+t_detail_feature + d_feature)
        web_results = return_search_result(result,feature_space)

        pagecount =  int(request.form['pagecount'])

        testid =  request.form['testid']

        history = pickle.load(open( "./resources/"+testid+".p", "rb" ))
        history[testid].append((pagecount,query,[],"",str(datetime.now())))
        pickle.dump(history, open( "./resources/"+testid+".p", "wb" ) )

        session['testid'] = testid

        pagecount += 1
        session['pagecount'] = pagecount
        pickle.dump(web_results, open( "./resources/info.p", "wb" ) )
        return redirect(url_for('web'))
    if request.method == 'GET':
        pagecount = session['pagecount']
        testid = session['testid']
        return render_template('query.html',pagecount = pagecount, testid = testid)


    return render_template('query.html')


############# Regular Query ##############

@app.route('/regular_query', methods=['GET', 'POST'])
def regular_query():

    if request.method == 'POST':
        query =  request.form['query']
        wordlist = load_file_tokens(query)
        (t_feature,t_detail_feature,d_feature) = build_initial_feature(wordlist)
        result = compute_similarity(feature_space,t_feature+t_detail_feature + d_feature)
        web_results = return_search_result(result,feature_space)

        pagecount =  int(request.form['pagecount'])

        testid =  request.form['testid']

        history = pickle.load(open( "./resources/"+testid+".p", "rb" ))
        history[testid].append((pagecount,query,[],str(datetime.now())))
        pickle.dump(history, open( "./resources/"+testid+".p", "wb" ) )

        session['testid'] = testid

        pagecount += 1
        session['pagecount'] = pagecount
        pickle.dump(web_results, open( "./resources/info.p", "wb" ) )
        return redirect(url_for('regular_web'))
    if request.method == 'GET':
        pagecount = session['pagecount']
        testid = session['testid']
        return render_template('regular_query.html',pagecount = pagecount, testid = testid)
    return render_template('regular_query.html')


@app.route('/regular_web', methods=['GET', 'POST'])
def regular_web():

    if request.method == 'POST':

        isfinish = request.form['finish']

        input_update_list = request.form['inputupdate']


        testid = request.form['testid']
        pagecount = int(request.form['pagecount'])
        #### Comment Out for Experiment
        leng = int(request.form['leng'])

        weblist = []
        for i in xrange(leng):
            key = 'u'+str(i)
            web = request.form[key]
            weblist.append(web)

        # selectedlist = []
        # for i in xrange(leng):
        #
        #     key = 's'+str(i)
        #
        #     selval = request.form[key]
        #
        #     if selval == 'yes':
        #         selectedlist.append(i)
        #
        # selectedwebs = [weblist[i] for i in selectedlist]

        if isfinish == "yes":

            history = pickle.load(open( "./resources/"+testid+".p", "rb" ))
            history[testid].append(("Final","",weblist,str(datetime.now())))
            f = open("./resources/"+testid+".txt",'w')

            for (x,y,z,w) in history[testid]:
                f.write('Step:' + str(x)+'\n')
                f.write('Query:' + y+'\n')
                f.write('Weblist:' + '\t'.join(z)+'\n')
                f.write('Time:' + w + '\n')


            pickle.dump(history, open( "./resources/"+testid+".p", "wb" ) )

            return redirect(url_for('first'))



        else:

            history = pickle.load(open( "./resources/"+testid+".p", "rb" ))
            history[testid].append((pagecount,input_update_list,[],str(datetime.now())))
            pickle.dump(history, open( "./resources/"+testid+".p", "wb" ) )
            pagecount += 1
            (t_feature,t_detail_feature,d_feature) = build_updated_feature_vector_interactive(input_update_list,"", [])
            result = compute_similarity(feature_space,t_feature+t_detail_feature + d_feature)
            web_results = return_search_result(result,feature_space)


            return render_template('regular_web.html',weblist =  web_results,length = len(web_results),pagecount = pagecount, testid = testid, oldquery = input_update_list)
###### End Comment Here
        #return redirect(url_for('hello'))
    elif request.method == 'GET':
        print "I am in GET"
        testid = session['testid']
        pagecount = session['pagecount']
        web_results = pickle.load(open( "./resources/info.p", "rb" ))
        history = pickle.load(open( "./resources/"+testid+".p", "rb" ))
        (oldpagecount,oldquery,oldweblist,oldtime) = history[testid][-1]
        return render_template('regular_web.html',weblist =  web_results,length = len(web_results),pagecount = pagecount, testid = testid,oldquery = oldquery)



def cosine_similarity(X,Y):
	X_sq = math.sqrt(sum( i**2 for i in X))
	Y_sq = math.sqrt(sum( i**2 for i in Y))
	if X_sq == 0 or Y_sq == 0:
		return 0.0
	X_Y = sum(a*b for a,b in zip(X,Y))
	return 1.0*X_Y/(X_sq*Y_sq)

def load_file_tokens(query):
	replaced = re.sub("[^0-9a-zA-Z ]"," ",query).lower()
	wordlist = replaced.split()
	return wordlist

def build_initial_feature(wordlist):
    t_feature = [0]*len(stemmed_text_features)
    d_feature = [0]*len(desc_features)
    t_detail_feature = [0]*len(stemmed_text_detail_features)



    # for i in xrange(len(text_features)):
    #     if text_features[i] in wordlist:
    #         t_feature[i] = 1
    #
    # for i in xrange(len(text_detail_features)):
    #     if text_detail_features[i] in wordlist:
    #         t_detail_feature[i] = 1


    for item in wordlist:
        if item in mapping_stemmed_text_features:
            token = mapping_stemmed_text_features[item]
            position = stemmed_text_features.index(token)
            t_feature[position] = 1

    for item in wordlist:
        if item in mapping_stemmed_text_detail_features:
            token = mapping_stemmed_text_detail_features[item]
            position = stemmed_text_detail_features.index(token)
            t_detail_feature[position] = 1


    for i in xrange(len(desc_features)):
        token_length = len(desc_features[i].split(" "))
        if token_length == 1:
            if desc_features[i] in wordlist:
                d_feature[i] = 1
        if token_length > 1:
            target_tokens = desc_features[i]
            for j in xrange(0, len(wordlist) - token_length + 1):
                tokens = " ".join(wordlist[j:j + token_length])
                if tokens == target_tokens:
                    d_feature[i] = 1

    return (t_feature, t_detail_feature,d_feature)
### To Do: Build feature vector for update
def build_updated_feature_vector_interactive(input_update_list,update_list, select_webs):


    update_words = load_file_tokens(update_list)
    input_update_words = load_file_tokens(input_update_list)

    for x in input_update_words:
        if x not in update_words:
            update_words.append(x)
    print update_words

    (self_t_feature, self_t_detail_feature,self_d_feature) = build_initial_feature(update_words)

    for item in select_webs:
        (t_feature,t_detail_feature,d_feature,non_professional,non_professional_detail) = feature_space[item+".html"]
        for i in xrange(len(t_feature)):
            if t_feature[i] == 1 and self_t_feature[i] == 0:
                self_t_feature[i] == 1
        for i in xrange(len(t_detail_feature)):
            if t_detail_feature[i] == 1 and self_t_detail_feature[i] == 0:
                self_t_detail_feature[i] == 1
        for i in xrange(len(d_feature)):
            if d_feature[i] == 1 and self_d_feature[i] == 0:
                self_d_feature[i] == 1

    return (self_t_feature, self_t_detail_feature,self_d_feature)


####

def compute_similarity(feature_space,query_feature):

    result = []
    for k,v in feature_space.iteritems():
        result.append((k,cosine_similarity(query_feature,v[0]+v[1]+v[2])))

    result = sorted(result,key=itemgetter(1),reverse=True)
    #print result
    return result

def return_search_result(results,feature_space):
    text_terms = []
    desc_terms = []
    text_detail_terms = []
    weblist = results[:10]
    #print title_dict
    result_list = []
    print len(text_features)
    print len(desc_features)
    for (x,y) in weblist:
        (t_feature,t_detail_feature,d_feature,non_professional, non_professional_detail) = feature_space[x]
        #temp_term_list = []
        #detail_term_list = []
        #temp_t_list = []
        temp_d_list = []

        # for i in xrange(len(t_feature)):
        #     if t_feature[i] == 1 and (text_features[i],1) not in text_terms:
        #         text_terms.append((text_features[i],1))
        #         temp_term_list.append(text_features[i])
        #         temp_t_list.append(text_features[i])
        #
        #
        # for i in xrange(len(t_detail_feature)):
        #     if t_detail_feature[i] == 1 and (text_detail_features[i],2) not in text_detail_terms:
        #         text_detail_terms.append((text_detail_features[i],2))
        #         detail_term_list.append(text_detail_features[i])



        for i in xrange(len(d_feature)):
            if d_feature[i] == 1 and desc_features[i] not in temp_d_list:
                #desc_terms.append((desc_features[i],3))
                #temp_term_list.append(desc_features[i])
                temp_d_list.append(desc_features[i])


        (t,c) = title_dict[x[7:]]
        if len(t) < 9:
            title = " ".join(t)
        else:
            title = " ".join(t[:9])+"..."


        if len(c) < 30:
            content = " ".join(c)+"..."
        else:
            content = " ".join(c[:30])+ "..."


        print content
        title = title.replace('\"', '\'')
        content = content.replace('\"', '\'')
        print content



        result_list.append((x[:-5],title,content,non_professional_detail,non_professional,temp_d_list))


    return (result_list )























if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
