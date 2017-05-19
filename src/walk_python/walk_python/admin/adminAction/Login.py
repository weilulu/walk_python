# -*- coding: UTF-8 -*-
'''
Created on 2017.4.3

@author: W.lu
'''

from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
from django import forms

from walk_python.admin.adminService import service
from walk_python.admin.adminDomain import adminUser

def toLogin(request):
    print '>>>to login'
    now = datetime.now()
    return render_to_response('user/login.html',{'test':now},context_instance=RequestContext(request))

class Login(forms.Form):
    print 'test-----------' 
    userName = forms.CharField()
    password = forms.CharField() 
    def clean(self):
        cleaned_data = self.cleaned_data
        userName = cleaned_data.get('userName')
        if not userName:
            self._error['userName'] = 'user name is empty!'
        password = cleaned_data.get('password')
        if not password:
            self._error['password'] = 'password is empty!'
        return cleaned_data

def index(request):
    data = Login(request.POST)
    flag = data.is_valid()
    print 'flag:%s' % flag
    if flag:
        info = data.cleaned_data
        u = adminUser.adminInfo.convertToAdminUser(info)
        service.queryAdmin(u)
    return render_to_response('user/start.html',{'test':''},context_instance=RequestContext(request))
