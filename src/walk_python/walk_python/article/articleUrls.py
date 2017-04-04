# -*- coding: UTF-8 -*-
'''
Created on 2017年4月2日

@author: Administrator
'''

from django.conf.urls.defaults import patterns
from walk_python.article.articleAction import writeAction

urlpatterns = patterns('',
                       (r'^startWrite',writeAction.startWrite),
                       (r'^write',writeAction.articleCreate),
                       )

