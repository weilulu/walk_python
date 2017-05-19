# -*- coding: UTF-8 -*-
'''
Created on 2017.4.3

@author: W.lu
'''
from walk_python.article.articleDao import articleDao
from walk_python.article.blogDomain.articleDomain import articleInfo
def saveArticle(articleParam):
    if articleParam and isinstance(articleParam,articleInfo):
        last_id = articleDao.saveArticle(articleParam)
        if last_id:
            return last_id
    return None    
