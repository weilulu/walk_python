'''
Created on 2017.7.6

@author: W.lu
'''

import redis

CATEGORY_REDIS_KEY_PRE = 'category_key_pre_'
CATEGORY_REDIS_KEY = 'category_key_'
TAG_REDIS_KEY_PRE = 'tag_key_pre_'
TAG_REDIS_KEY = 'tag_key_'

def getRedisConn():
    try:
        conn = redis.StrictRedis(
            host='59.110.216.62',
            port=6379,
            password='a9564ebc3289b7a14551baf8ad5ec60a')
        print conn
        return conn
    except Exception as ex:
        print 'redis exception',ex
        
def hashSave(key1,key2,data):
    conn = getRedisConn();
    r = conn.pipeline()
    _id = data.getPrTy('id')
    title = data.getPrTy('title')
    create_time = data.getPrTy('create_time')
    r.hset(key1,CATEGORY_REDIS_KEY_PRE + 'id',_id)
    r.hset(key1,CATEGORY_REDIS_KEY_PRE + 'title',title)
    r.hset(key1,CATEGORY_REDIS_KEY_PRE + 'create_time',create_time)
  
    r.hset(key2,TAG_REDIS_KEY_PRE + 'id',_id)
    r.hset(key2,TAG_REDIS_KEY_PRE + 'title',title)
    r.hset(key2,TAG_REDIS_KEY_PRE + 'create_time',create_time)
    r.execute()
    print 'key1:%s,key2:%s,data:%s' % (key1,key2,data)
    
            
if __name__ == '__main__':
    hashSave('1', '2', 'test')            