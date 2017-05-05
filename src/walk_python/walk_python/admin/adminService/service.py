'''
Created on 2017.5.4

@author: W.lu
'''

from walk_python.admin.adminDao import adminDao
def queryAdmin(articleParam):
    rs = {}
    for key,value in articleParam.items():
        rs[key] = value
    if articleParam:
        adminDao.queryAdmin(rs);
        
    
