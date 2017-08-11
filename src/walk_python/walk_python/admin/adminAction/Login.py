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
        userId = service.queryAdmin(u)
        print 'userId:%s' % userId
        if userId:
            name = u.getPrTy('userName')
            service.saveLoginer(userId,name)
            #return render_to_response('user/start.html',{'userName':name},context_instance=RequestContext(request))
            return render_to_response('user/index.html',{'userId':userId,'userName':name},context_instance=RequestContext(request))
        else:
            info = 'name or pwd was wrong!'
            return render_to_response('user/login.html',{'errorInfo':info},context_instance=RequestContext(request))
def welcome(request):
    loginId = request.GET['id']
    print 'login id %s:' % loginId
    name = service.getLoger(loginId)
    print name
    if name:
        return render_to_response('user/index.html',{'userId':loginId,'userName':name},context_instance=RequestContext(request))
    else:
        return render_to_response('user/login.html',{'errorInfo':''},context_instance=RequestContext(request))
def write(request):
    loginId = request.GET['id']
    print 'login id %s:' % loginId
    name = service.getLoger(loginId)
    if name:
        return render_to_response('article/write.html',{'userId':loginId,'userName':name},context_instance=RequestContext(request))
    else:
        return render_to_response('user/login.html',{'errorInfo':''},context_instance=RequestContext(request))