'''
Created on 2017.5.4

@author: W.lu
'''

from walk_python.dbtables import models

def queryAdmin(dictParam):
    if dictParam:
        #rs = {}
        print(dictParam.get('userName'))
        selSql = models.adminR.select().where(dictParam)
        result = models.executeSelectSql(selSql)
        print(result)