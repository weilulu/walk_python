# -*- coding: UTF-8 -*-
'''
Created on 2017.4.4

@author: W.lu
'''
from datetime import datetime
from sqlalchemy.engine.result import RowProxy 
class BaseObject(object):
    
    __slots__ = ('_prykeys')
    _prykeys = {'_prykeys':dict,'is_init':bool}
    
    def __init__(self):
        self.is_init = True
        
    def __getattr__(self,key):
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
        """
        对象内部的方法
        """
        if key in self.__slots__:
            vType = self._prykeys[key]
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
            #raise AttributeError
    
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
    __slots__=('id','title','type','author','summary','content','post_time','is_init','_prykeys')
    _prykeys={'id':(int,long),'title':str,'type':(int,long),'author':str,'summary':str,'content':str,'post_time':datetime,'is_init':bool,'_prykeys':dict}
    
    def __init__(self):
        BaseObject.__init__(self)
        self.id = 0
        self.title = ''
        self.type = 0
        self.author = ''
        self.summary = ''
        self.content = ''
        self.post_time = None
        self.is_init = True     
        
    @classmethod
    def convertToArticle(cls,rss):
        rs = None
        if rss and isinstance(rss,(RowProxy,dict)):
            rs = cls()
            for key,value in rss.items():
                if isinstance(key,unicode):
                    key = key.encode('utf-8')
                if isinstance(value,unicode):
                    value = value.encode('utf-8')
                rs.setPrTy(key,value)
            
        return rs       
    
    def setPrTy(self,key,value):
        """
        设置文章的某一个属性
        @key    type:str 
            文章的属性名称
        @value  type:依据属性的值的属性做判断
            文章属性的值
        """
        flag = False
        try:
            setattr(self,key,value)
            flag = True
        except Exception,data:
            print data
        return flag
    
    def getPrTy(self,key):
        """
        取得直博内容的某一个属性值
        @key    type:str 
            直博内容的属性名称
        """
        
        try:
            rs = getattr(self,key)
        except Exception,data:
            print data
            rs = None
        return rs
    def getDictKeys(self,isSimple=True):
        """
        取得对象转成字典时的keys
        @isSimple   type:bool
            是否是简单和只包括内容的keys
        """
        
        if isSimple:
            keys = self._prykeys.keys()
            #keys.remove('is_init')
            keys.remove('_prykeys')
            #keys.remove('summary')
            #keys.remove('content')
            keys.remove('id')
            return keys
        else:
            #keys = ['id']
            keys = self._prykeys.keys();
            return keys
    
