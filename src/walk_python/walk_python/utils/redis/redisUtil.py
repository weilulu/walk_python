# -*- coding: UTF-8 -*-
'''
Created on 2017.7.6

@author: W.lu
'''

import redis
import time
import codecs

CATEGORY_REDIS_KEY_PRE = 'category_key_pre_'
CATEGORY_REDIS_KEY = 'category_key_'
TAG_REDIS_KEY_PRE = 'tag_key_pre_'
TAG_REDIS_KEY = 'tag_key_'

def getRedisConn():
    try:
        conn = redis.StrictRedis(
            #host='localhost',
            #port=6379
            host='59.110.216.62',
            port=6379,
            password='a9564ebc3289b7a14551baf8ad5ec60a'
            )
        print conn
        return conn
    except Exception as ex:
        print 'redis exception',ex
        
def hashSave(key,data):
    conn = getRedisConn()
    ctime = data.getPrTy('create_time')
    t = time.strptime(ctime, '%Y-%m-%d %H:%M:%S')
    timeScore = time.mktime(t)
    d = {'id':data.getPrTy('id'),'title':data.getPrTy('title'),'create_time':t}
    #jsonStr = json.dumps(d)
    print 'timeS:%s,jsonStr:%s' % (timeScore,d)
    conn.zadd(key,timeScore,d)

def strSave(key,value):
    '''
       save,type string
    '''
    conn = getRedisConn()
    flag = conn.set(key, value)
    print 'strsave flag:%s' % flag 
def strGet(key):
    '''
       get,type string
    '''
    conn = getRedisConn()
    return conn.get(key)
       
def getV(key1,key2):
    conn = getRedisConn();
    print(conn.hget(key1,key2)) 
    print(conn.hgetall(key1))
 
def testRedis():
    conn = getRedisConn()
    conn.hset('key1','key2','value') 
def getStrKey(key):
    conn  = getRedisConn()
    print conn.get(key)   
if __name__ == '__main__':
    #testRedis()
    #getV('key1','key2')
    '''
    conn = getRedisConn()
    t = time.strptime('2017-07-10 10:26:57', '%Y-%m-%d %H:%M:%S')
    t1 = time.strptime('2017-07-10 10:38:25', '%Y-%m-%d %H:%M:%S')
    score = time.mktime(t)
    score1 = time.mktime(t1)
    d={'id':1,'title':codecs.encode('汉字', 'utf-8'),'create_time':'2017-07-10 10:26:57'}
    d1={'id':2,'title':'title2','create_time':'2017-07-10 10:38:25'}
    conn.zadd('life',score,d)
    conn.zadd('life',score1,d1)
    
    
    print(score)            
    print(score1)            
    '''
    getStrKey('1') 