# -*- coding: UTF-8 -*-
'''
Created on 2017.4.4

@author: W.lu
'''
from sqlalchemy.engine.result import RowProxy 

from walk_python.baseObject.baseDomain import BaseObject

     
class adminInfo(BaseObject):
    __slots__=('id','userName','password','type','is_init','_prykeys')
    _prykeys={'id':(int,long),'userName':str,'password':str,'type':(int,long),'is_init':bool,'_prykeys':dict}
    
    def __init__(self):
        BaseObject.__init__(self)
        self.id = 0
        self.userName = ''
        self.password = ''
        self.type = 0
        self.is_init = True     
        
    @classmethod
    def convertToAdminUser(cls,rss):
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
       
        flag = False
        try:
            setattr(self,key,value)
            flag = True
        except Exception,data:
            print data
        return flag
    
    def getPrTy(self,key):
       
        
        try:
            rs = getattr(self,key)
        except Exception,data:
            print data
            rs = None
        return rs
    def getDictKeys(self,isSimple=True):
       
        
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
            #keys.remove('post_time')
            return keys
    
