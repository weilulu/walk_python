# -*- coding: UTF-8 -*-
'''
Created on 2017.4.4

@author: W.lu
'''
from datetime import datetime
from sqlalchemy.engine.result import RowProxy 

from walk_python.baseObject.baseDomain import BaseObject

     
class articleInfo(BaseObject):
    __slots__=('id','title','author','summary','content','create_time','post_time','is_init','_prykeys')
    _prykeys={'id':(int,long),'title':str,'author':str,'summary':str,'content':str,'create_time':str,'post_time':datetime,'is_init':bool,'_prykeys':dict}
    
    def __init__(self):
        BaseObject.__init__(self)
        self.id = 0
        self.title = ''
        self.author = ''
        self.summary = ''
        self.content = ''
        self.create_time = ''
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
            keys.remove('id')
            keys.remove('post_time')
            return keys
    
