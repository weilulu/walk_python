# -*- coding: UTF-8 -*-
'''
Created on 2017年4月4日

@author: Administrator
'''
from sqlalchemy import *
import datetime

class BaseObject(object):
    
    __slots__ = ('_prykeys')
    _prykesy = {'_prykeys':dict,'is_init':bool}
    
    def __init__(self):
        self.is_init = True
        
    def __getattr(self,key):
        if key in self.__slots__:
            rs = None
            try:
                rs = object.__getattribute__(self,key)
            except Exception,data:
                print 'getattr ',data
                rs = None
            return None
        else:
            print 'get attr the object has not the attr ',key
            raise AttributeError # like throws exception in Java
        
    def __setattr__(self,key,value):
        if key in self.__slots__:
            vType = self._prykesy[key]
            if isinstance(value,vType) or (value is None and vType in (str,datetime)):
                object.__setattr__(self,key,value)
                if key != 'is_init' and 'is_init' in self.__slots__:
                    if self.is_init:
                        object.__setattr__(self,'is_init',False)
            else:
                print 'the value type is wrong!'
                raise AttributeError
        else:
            print 'set attr the object has the Attribute!',key,value
            
    def _contains__(self,key):
        if key in self.__slots__:
            return True
        return False
    
    def __getitem__(self,key):
        if key in self:
            return getattr(self,key)
        else:
            print 'get item the object has no attr ',key
            raise AttributeError
    
    def __setitem__(self,key,value):
        if key in self:
            vType = self._prykeys[key]
            if isinstance(value,vType):
                object.__setattr__(self,key,value)
                if 'is_init' in self.__slots__:
                    if self.is_init:
                        object.__setattr__(self,'is_init',False)
            else:
                print 'the value type is wrong!'
                raise AttributeError
        else:
            print 'setitem the object has not the attr!',key,value
            #raise AttributeError   
            
    def convertToDict(self,keyList=None,isJson=False):
        rs = {}
        if not self.is_init:
            keys = []
            if keyList is None or not isinstance(keyList, list):
                keys = self.__slots__
            else:
                keys = keyList
            for key in keys:
                if key not in ('_prykeys','is_init'):
                    tmp = getattr(self,key)
                    if isJson and isinstance(tmp, datetime):
                        tmp = str(tmp)
                    rs[key] = tmp
        return rs
     
class articleInfo(BaseObject):
    __slot__=('id','title','type','author','summary','post_time')
    _prykesy={'id':(int,long),'title':str,'type':int,'author':str,'summary':str,'post_time':datetime}
    
    def __init__(self):
        BaseObject.__init__(self)
        self.id = 0
        self.title = ''
        self.type = 0
        self.author = ''
        self.summary = ''
        self.post_time = None       
        
    @classmethod
    def convertToArticle(cls,rss):
        rs = None
        if rss and isinstance(rss, RowProxy,dict):
            rs = cls()
            for key,value in rss.items():
                if isinstance(key, unicode):
                    key = key.encode('utf-8')
                if isinstance(value, unicode):
                    value = value.encode('utf-8')
                rs.setPrTy(key,value)
        return rs                                                         