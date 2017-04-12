#-*- coding : UTF-8 -*-
'''
Created on 2017.4.3

@author: W.lu
'''

from walk_python.dbtables import models
from walk_python.article.blogDomain.articleDomain import articleInfo

def saveArticle(articleParam):
    if articleParam and isinstance(articleParam,articleInfo):
        dd = articleParam.convertToDict(keyList=articleParam.getDictKeys(False))
        selSql = models.articleW.insert().values(dd)
        rss = models.executeInsertSql(selSql)
        if rss:
            print 'last id >>>>'
            print rss.lastrowid
            print 'last id ----'
            return rss.lastrowid
    return None
    
