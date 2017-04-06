# -*- coding: UTF-8 -*-
'''
Created on 2017年4月3日

@author: Administrator
'''
from django.shortcuts import render_to_response
import datetime
from django import forms
#from django.forms.models import cleaned_data
from walk_python.article.blogDomain import articleDomain
from walk_python.article.blogDomain.articleDomain import articleInfo
from walk_python.article.articleService import service
from walk_python.article.utils import StringUtil
from django.template import RequestContext

def startWrite(request):
    print 'test>>>>>'
    now = datetime.datetime.now()    
    return render_to_response('article/article_write.html',{'test':now},context_instance=RequestContext(request))

class WriteArticle(forms.Form):
    print 'start here.........'
    title = forms.CharField()
    type = forms.IntegerField()
    author = forms.CharField()
    content = forms.Field()
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        if not title:
            self._errors['title'] = 'title is empty!'
        type = cleaned_data.get('type')
        if not isinstance(type, (int,long)):
            type = 0    #default value 0
        author = cleaned_data.get('author')
        if not author:
            self._errors['author'] = 'author is empty!'
        content = cleaned_data.get('content')
        if not content:
            self._errors['content'] = 'content is empty!'
        
        return cleaned_data
    
def articleCreate(request):
    print 'articleCreate start....'

    form = WriteArticle(request.POST)
    flag = form.is_valid()
    print (flag)
    if flag:
        ac = form.cleaned_data
        ta = articleDomain.articleInfo.convertToArticle(ac)
        c = ta
        StringUtil.escapeScript(c)
        ta.setPrTy('content',c)
        last_id = service.saveArticle(ta)
        
    return render_to_response('test/test.html',{'test':'test'},context_instance=RequestContext(request))

    