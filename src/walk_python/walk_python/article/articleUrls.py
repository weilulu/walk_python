# -*- coding: UTF-8 -*-
'''
Created on 2017年4月2日

@author: W.lu
'''

from django.conf.urls import patterns, url, include
from walk_python.article.articleAction import WriteArticle

urlpatterns = patterns('',
                       (r'^startWrite',WriteArticle.startWrite),
                       (r'^write',WriteArticle.articleCreate),
                       )

