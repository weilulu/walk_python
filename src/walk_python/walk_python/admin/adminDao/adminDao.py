'''
Created on 2017.5.4

@author: W.lu
'''

from walk_python.dbtables import models
from walk_python.admin.adminDomain.adminUser import adminInfo
from sqlalchemy import select,and_

def queryAdmin(userInfo):
    if userInfo and isinstance(userInfo, adminInfo):
        selSql = select([models.adminR.c.id]).where(models.adminR.c.userName==userInfo.getPrTy('userName')).where(models.adminR.c.password==userInfo.getPrTy('password'))
        try:
            rs = models.executeSelectSql(selSql)
        except Exception,data:
            print data
        
        
        print '-----'