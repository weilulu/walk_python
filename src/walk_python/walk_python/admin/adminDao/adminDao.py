'''
Created on 2017.5.4

@author: W.lu
'''

from walk_python.dbtables import models
from walk_python.admin.adminDomain.adminUser import adminInfo
from sqlalchemy import select,and_

def queryAdmin(userInfo):
    if userInfo and isinstance(userInfo, adminInfo):
        name = userInfo.getPrTy('userName')
        pwd = userInfo.getPrTy('password')
        selSql = select([models.adminR.c.id]).where(models.adminR.c.userName==name) \
                                             .where(models.adminR.c.password==pwd) \
                                             .limit(1).offset(0)
        #selSql = select([models.adminR.c.id],and_(models.adminR.c.userName == name))                                     
        rs = models.getConnection().execute(selSql)
        if rs:
            for resultId in rs:
                return resultId['id']
        return None
    return None