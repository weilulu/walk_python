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
    category = forms.Field()
    author = forms.CharField()
    content = forms.Field()
    #tag = forms.Field()
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        if not title:
            self._errors['title'] = 'title is empty!'
        category = cleaned_data.get('category')
        if not category:
            self._errors['category'] = 'category is empty!'
        author = cleaned_data.get('author')
        if not author:
            self._errors['author'] = 'author is empty!'
        content = cleaned_data.get('content')
        if not content:
            self._errors['content'] = 'content is empty!'
        tag = cleaned_data.get('tag')
        #if not tag:
            #self._errors['tag'] = 'tag is empty!'
        return cleaned_data
    
def articleCreate(request):
    print 'articleCreate start....'

    data = WriteArticle(request.POST)
    print(data.errors)
    flag = data.is_valid()
    print (flag)
    if flag:
        ac = data.cleaned_data
        category = ac['category']
        #tag = ac['tag']
        ac.pop('category',None)
        #ac.pop('tag',None)
        ta = articleDomain.articleInfo.convertToArticle(ac)
        #flag = False
        content = StringUtil.escapeScript(ta.getPrTy('content'))
        summary = StringUtil.genSummary(content)
        ta.setPrTy('content',content)
        ta.setPrTy('summary',summary)
        articleEntity = service.saveArticle(ta)
        if articleEntity:
            service.saveCategory(articleEntity.getPrTy('id'),category)
            service.createIndex(articleEntity)
            service.saveCategoryInRedis(category,articleEntity)
            return render_to_response('article/post_success.html',{'last_id':articleEntity.getPrTy('id')},context_instance=RequestContext(request))
    return render_to_response('article/post_fail.html',{'error_info':'error'},context_instance=RequestContext(request))
 
    