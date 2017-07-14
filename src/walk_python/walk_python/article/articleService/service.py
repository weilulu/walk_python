'''
Created on 2017.4.3

@author: W.lu
'''
from walk_python.article.articleDao import articleDao
from walk_python.article.blogDomain.articleDomain import articleInfo
from walk_python.utils.elastic import search
from walk_python.utils.redis import redisUtil
import json
import time

def saveArticle(articleParam):
    '''
       1,save data in mysql
       2,index data with elastic
       3,add category/tags data within redis
    '''
    if articleParam and isinstance(articleParam,articleInfo):
        _time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))    
        articleParam.setPrTy('create_time',_time)      
        last_id = articleDao.saveArticle(articleParam)
        if last_id:
            articleParam.setPrTy('id',last_id)
            return articleParam
            '''
            articleDict = articleParam.convertToDict(keyList=articleParam.getDictKeys(False))
            articleDict['id'] = last_id
            articleJson = json.dumps(articleDict)
            # index with elastic
            indexFlag = search.createArticleIndex(articleJson,last_id)
            if not indexFlag:
                print 'the id of mysql is:%s' % (last_id)
            #add data into redis
            #articleDict = {'id':last_id,'title':articleParam.getPrTy('title'),'time':time}
            articleParam.setPrTy('id',last_id)
            category_key= articleParam.getPrTy('category')
            tag_key = articleParam.getPrTy('tag')
            redisUtil.hashSave(category_key,tag_key,articleParam)
        return last_id
            '''
        return None
    return None
def saveCategory(article_id,category):
    articleDao.saveCategory(article_id,category)
def createIndex(article):
    '''
    index with elastic
    '''
    articleDict = article.convertToDict(keyList=article.getDictKeys(False))
    articleJson = json.dumps(articleDict)
    docId = article.getPrTy('id')
    indexFlag = search.createArticleIndex(articleJson,docId)
    if not indexFlag:
        print 'the id of mysql is:%s' % (docId)
    
    
def saveCategoryInRedis(category_key,article):
    '''
    add data into redis
    '''
    redisUtil.hashSave(category_key,article)    
    