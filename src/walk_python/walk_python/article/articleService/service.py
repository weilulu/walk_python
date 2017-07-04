# -*- coding: UTF-8 -*-
'''
Created on 2017.4.3

@author: W.lu
'''
from walk_python.article.articleDao import articleDao
from walk_python.article.blogDomain.articleDomain import articleInfo
from walk_python.utils.elastic import search
import json

def saveArticle(articleParam):
    if articleParam and isinstance(articleParam,articleInfo):
        last_id = articleDao.saveArticle(articleParam)
        if last_id:
		    articleDict = articleParam.convertToDict(keyList=articleParam.getDictKeys(False))
		    articleJson = json.dumps(articleDict)
		    indexFlag = search.createArticleIndex(articleJson,last_id)
		    if not indexFlag:
			   print 'the id of mysql is:%s' % (last_id)
        return last_id
    return None    
