# -*- coding: UTF-8 -*-
'''
Created on 2017.5.2

@author: W.lu
'''

from django.conf.urls import patterns
from walk_python.admin.adminAction import Login
from django.contrib.auth import login

urlpatterns = patterns('',
                       (r'^login',Login.toLogin),
                       (r'^index',Login.index),
                       (r'^welcome',Login.welcome),
                       (r'^write',Login.write),
                       )

