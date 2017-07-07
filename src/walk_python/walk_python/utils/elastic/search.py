# -*- coding: UTF-8 -*-

'''
Created on 2017.7.3

@author: W.lu
'''

#import requests
from elasticsearch import Elasticsearch
#import json

es = Elasticsearch([{'host':'localhost','port':9200}])

def createArticleIndex(jsonString,docId):
    print(jsonString)
    try:
	    res = es.create(index="article_index",doc_type="article_content",id=docId,body=jsonString)
        #print(res['created'])
	    return res['created']
    except Exception,data:
	    print data
    return False
    
    	
def test():
    doc = {"author":"kimchy","text":"Elasticsearch cool. bonsai cool."}
    try:
	    res = es.create(index="test_index",doc_type="tweet",id=1,body=doc)
	    print(res['created'])
    except Exception,data:
	    print data
	
def getArticleIndex():
    res = es.get(index="article_index",doc_type="article_content",id=2)
	
    print(res)
	
	
if __name__ == '__main__':
	#test()
	getArticleIndex()
    #pass