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
def saveCategory(article_id,category):
    _dict = {'article_id':article_id,'name':category}
    sql = models.categoryW.insert().values(_dict)
    rss = models.executeInsertSql(sql)
    if rss:
        print rss.lastrowid
             