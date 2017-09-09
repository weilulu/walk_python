# -*- coding: UTF-8 -*-
'''
Created on 2017.7.6

@author: W.lu
'''
from pymongo import MongoClient
from bson.objectid import ObjectId


def getDB():
    client = MongoClient("localhost",27017)
    db = client.walk_management
    return db

def addTest():
    db = getDB()
    if db:
        #articleInfo = db.article_info
        #posts = db.posts
        posts= db.ArticleInfo
        articleInfo = {"title":"回想里的微笑","content":"你的微笑，在我的回忆里，很美","post_time":"1988-10-2"}
        post_id = posts.insert(articleInfo)
        print post_id

def queryTest():
    db = getDB()
    if db:
        posts = db.posts
        print posts
        obj = posts.find_one()
        obj_id = obj["_id"]
        result = posts.find_one({"_id":obj_id})
        print result

def queryAllTest():
    db = getDB()
    if db:
        for data in db.posts.find():
            print data

def queryDataById():
    id = '59b3a22339ec1d1b2c5eae5a'
    db = getDB()    
    if db:
        posts = db.posts
        print posts.find_one({"_id":ObjectId(id)})                 
if __name__ == '__main__':
    addTest() #59b3a19839ec1d0a48b3f803  59b3a22339ec1d1b2c5eae5a
    #queryTest()
    #queryAllTest()
    #queryDataById()