#-*- coding : UTF-8 -*-
'''
Created on 2017.4.3

@author: W.lu
'''

from walk_python.dbtables import models

def saveArticle(articleParam):
    if not articleParam.is_init:
        dd = articleParam.convertToDict(keyList=articleParam.getDictKeys())
        selSql = models.articleW.insert().values(dd)
        rss = models.executeInsertSql(selSql)
        if rss:
            print 'last id >>>>'
            print rss.lastrowid
            print 'last id ----'
            return rss.lastrowid
    return None
    
