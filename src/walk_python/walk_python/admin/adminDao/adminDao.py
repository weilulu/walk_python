'''
Created on 2017.5.4

@author: W.lu
'''

from walk_python.dbtables import models
from walk_python.admin.adminDomain.adminUser import adminInfo

def queryAdmin(userInfo):
    if userInfo and isinstance(userInfo, adminInfo):
        selSql = models.adminR.select().where(models.adminR.c.userName == userInfo.getPrTy('userName'))
        selSql = models.adminR.select().where(models.adminR.c.password == userInfo.getPrTy('password'))
        rs = models.executeSelectSql(selSql)
        print '-----'