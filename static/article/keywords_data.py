import csv
from collections import Counter
import operator
import pickle
import ast

#article1 = "/Users/GMK/Documents/Research/Facebook/data/article/NEW_final_out_10155584306476509.txt"
#article2 = "./NEW_final_out_10155699096601509.txt"
article3 = "./final_5550296508_10155749891186509.txt"
#article4 = "/Users/GMK/Documents/Research/Facebook/data/article/NEW_final_out_10155792006356509.txt"
article5 = "./final_15704546335_10155095856676336.txt"

def build_corpus(txtfile,wrtfile):
    f=open(txtfile,"r")
    keys_dic = {}
    for line in f.readlines():
        arr=eval(line)
        if keys_dic.has_key(arr[0]):
			keys_dic[arr[0]].append((arr[1],arr[2],arr[3]))
        else:
			keys_dic[arr[0]]=[(arr[1],arr[2],arr[3])]
    # read the file as a dictionary for each row ({header : value})

    #print keys_dic

    new_keys_dic = {}

    keys = keys_dic.keys()

    for x in keys:
        tempdocs= keys_dic[x]
        docs = []
        for (sentiment,document, ids) in tempdocs:
            if '&' in document:
                print document
                document = document.replace('&','and')
            docs.append((sentiment,document, ids))

        x=x.replace("'","")
        key_list = x.split(',')

        print key_list

        key_set = list(set([item.lower().strip() for item in key_list]))


        #print key_set
        removed_sub_key = []
        for i in xrange(len(key_set)):
            for j in xrange(len(key_set)):
                if key_set[i] in key_set[j] and i != j:
                    removed_sub_key.append(key_set[i])
                    break
        removed_sub_key_list = list(set(key_set)-set(removed_sub_key))
        #print removed_sub_key_list

        if len(removed_sub_key_list) == 1:
            new_keys_dic[removed_sub_key_list[0].upper()] = docs
        elif len(removed_sub_key_list) == 2:
            new_keys_dic[removed_sub_key_list[0].upper()+","+removed_sub_key_list[1].upper()] = docs
        elif len(removed_sub_key_list) == 3:
            new_keys_dic[removed_sub_key_list[0].upper()+","+removed_sub_key_list[1].upper()+","+removed_sub_key_list[2].upper()] = docs
        else:
            counted_terms = []
            for term in removed_sub_key_list:
                t_count = 0
                for (sentiment, sentence,index) in docs:
                    t_count += sentence.lower().count(term)
                counted_terms.append((term,t_count))
            #print counted_terms
            sorted_items = sorted(counted_terms, key=lambda x: x[1], reverse = True)
            #print sorted_items
            long_key_list = [sorted_items[0][0].upper(),sorted_items[1][0].upper(),sorted_items[2][0].upper()]
            long_key = ",".join(long_key_list)
            new_keys_dic[long_key] = docs

    fwrite = open(wrtfile, 'w+')
    for key in new_keys_dic.keys():
        for doc in new_keys_dic[key]:
            fwrite.write(str([key,doc[0],doc[1],doc[2]])+'\n')
    fwrite.close()

def build_corpus_control(txtfile,wrtfile):
    f=open(txtfile,"r")
    keys_dic = {}
    fwrite = open(wrtfile, 'w+')
    for line in f.readlines():
        temp_arr=ast.literal_eval(line)
        #temp_arr = eval(json.loads(line))
        #print temp_arr
        document = temp_arr[2]

        if '&' in document:
            print document
            document = document.replace('&','and')
            print document


        arr= [temp_arr[0],temp_arr[1],document,temp_arr[3]]
        print arr
        fwrite.write(str(arr)+'\n')

    fwrite.close()


if __name__ == "__main__":
    #build_corpus(article1,'NEW_1.txt')
    #build_corpus(article2,'NEW_4.txt')
    build_corpus(article3,'NEW_3.txt')
    #build_corpus(article4,'NEW_2.txt')
    build_corpus(article5,'NEW_5.txt')
    build_corpus(article3,'BALANCED_3.txt')
    #build_corpus(article4,'NEW_2.txt')
    build_corpus(article5,'BALANCED_5.txt')
    # build_corpus_control(article1,'C_NEW_1.txt')
    #build_corpus_control(article2,'C_NEW_4.txt')
    build_corpus_control(article3,'C_NEW_3.txt')
    #build_corpus_control(article4,'C_NEW_2.txt')
    build_corpus_control(article5,'C_NEW_5.txt')
