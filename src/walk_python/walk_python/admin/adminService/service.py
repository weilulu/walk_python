'''
Created on 2017.5.4

@author: W.lu
'''
from walk_python.admin.adminDomain.adminUser import adminInfo
from walk_python.admin.adminDao import adminDao
from walk_python.utils.redis import redisUtil

LOGIN_USER_ID = 'login_user_id_'

def queryAdmin(userInfo):
    if userInfo and isinstance(userInfo, adminInfo):
        userId = adminDao.queryAdmin(userInfo)
        return userId
         

def saveLoginer(userId,userName):
    if userId and userName:
        print '>>>start to save,userId:%s,name:%s' % (userId,userName)
        redisUtil.strSave(LOGIN_USER_ID + str(userId),userName)
             
def getLoger(loginId):
    if loginId:
        return redisUtil.strGet(LOGIN_USER_ID + str(loginId))                 
