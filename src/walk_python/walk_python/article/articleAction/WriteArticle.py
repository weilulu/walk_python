# -*- coding: UTF-8 -*-
'''
Created on 2017.4.3

@author: W.lu
'''
from django.shortcuts import render_to_response
import datetime
from django import forms
from walk_python.article.blogDomain import articleDomain
from walk_python.article.blogDomain.articleDomain import articleInfo
from walk_python.article.articleService import service
from walk_python.utils import StringUtil
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

    data = WriteArticle(request.POST)
    print(data.errors)
    flag = data.is_valid()
    print (flag)
    if flag:
        ac = data.cleaned_data
        ta = articleDomain.articleInfo.convertToArticle(ac)
        #flag = False
        content = StringUtil.escapeScript(ta.getPrTy('content'))
        summary = StringUtil.genSummary(content)
        ta.setPrTy('content',content)
        ta.setPrTy('summary',summary)
        last_id = service.saveArticle(ta)
        
    return render_to_response('article/post_success.html',{'last_id':last_id},context_instance=RequestContext(request))
'''    
def getArticleDetail(request):
    article_id = forms.IntegerField()
    result = service.getArticleById(article_id)
    detail = {}
    if result:
        detail = {"articleDetail",result}
    return render_to_response('article/article_detail.html',detail,context_instance=RequestContext(request))
'''    
    