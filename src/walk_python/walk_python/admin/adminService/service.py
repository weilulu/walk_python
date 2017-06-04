'''
Created on 2017.5.4

@author: W.lu
'''
from walk_python.admin.adminDomain.adminUser import adminInfo
from walk_python.admin.adminDao import adminDao

def queryAdmin(userInfo):
    if userInfo and isinstance(userInfo, adminInfo):
        count = adminDao.queryAdmin(userInfo)
        if count == 1:
            return True
        else:
            return False
         
         
    
