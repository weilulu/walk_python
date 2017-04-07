# -*- coding: UTF-8 -*-
'''
Created on 2017年4月3日

@author: W.lu
'''
from walk_python.article.articleDao import articleDao

def saveArticle(articleParam):
    if articleParam and articleParam.is_init:
        articleDao.saveArticle(articleParam)
        
    
        