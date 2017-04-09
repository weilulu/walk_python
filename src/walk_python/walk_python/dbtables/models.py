#-*- encoding: UTF-8 -*-
'''
Created on 2017.4.7

@author: W.lu
'''
from sqlalchemy import create_engine,MetaData
from sqlalchemy.sql.expression import Select,CompoundSelect,Insert,Update,Delete
from sqlalchemy.engine.result import RowProxy

dbr = create_engine("mysql://root:root@localhost:3306/walk-management?charset=utf8",pool_size=50,max_overflow=100,echo=True,pool_timeout=10,echo_pool=False,pool_recycle=3600)
dbw = create_engine("mysql://root:root@localhost:3306/walk-management?charset=utf8",pool_size=50,max_overflow=100,echo=False,pool_timeout=10,echo_pool=False,pool_recycle=3600)

metaRead = MetaData(bind=dbr,reflect=True)
metaWrite = metaRead

def getDB(readed=False):
    if readed:
        global dbw
        return dbw
    else:
        global dbr
        return dbr
def getConnection(readed=False):
    conn = None
    db = getDB(readed)
    if db:
        try:
            conn = db.conn()
            conn.ping(True)
        except:
            if readed:
                print 'dbw cannot connection!'
            else:
                print 'dbw cannot connection!'
            conn = None
    else:
        print 'get DB wrong!'
    return conn
def closeConnection(conn,readed=False):
    if conn:
        if conn.closed:
            print 'the connection is already closeded!'
        else:
            conn.close()
    else:
        print 'the connection is NULL!!!' 
def connectionFunctionNew(isRead=False,connectionKey='conn'):
    def connectionFunc(func):
        def Func(*args,**argss):
            conn = getConnection(isRead)
            argss[connectionKey] = conn
            dd = func(*args,**argss)
            closeConnection(conn)
            return dd
        return Func
    return connectionFunc
@connectionFunctionNew(False, 'conn')
def executeSelectSql(selectSql,isFetchAll=False,conn=None,defaultReturn=None):
    from __builtin__ import str
    from _ast import Str
    if selectSql:
        if isinstance(selectSql,Select) or isinstance(selectSql,CompoundSelect):
            if conn:
                rss = None
                try:
                    if isFetchAll:
                        rss = conn.execute(selectSql).fetchall()
                    else:
                        rss = conn.execute(selectSql).fetchone()    
                except Exception,data:
                    print data
                    rss = None
                finally:
                    closeConnection(conn)
                if rss:
                    if not isFetchAll:
                        rs = {}
                        if isinstance(rss,RowProxy):
                            for k,v in rss.items():
                                k = str(k)
                            rs[k] = v        
                        return rs
                    else:
                        rs = []
                        for val in rss:
                            if isinstance(val,RowProxy):
                                trs = {}
                                for k,v in val.items():
                                    if isinstance(k,unicode):
                                        k = Str(k)
                                    trs[k] = v
                                if trs:
                                    rs.append(trs)
                        return rs
                    return rss
                return defaultReturn
@connectionFunctionNew(True, 'conn')
def executeInsertSql(sql,conn=None):
    from cgitb import text
    if sql and isinstance(sql, Insert,Update,str,Delete):
        if conn:
            rs = None
            try:
                if isinstance(sql, str):
                    sql = text(sql)
                rs = conn.excute(sql)
            except Exception,data:
                print data
                print 'excute insert(update) sql exception!!!'
                rs = None
            finally:
                closeConnection(conn)
            if rs:
                return rs
    return None            



articleW = metaWrite.tables['article_info']
articleR = metaRead.tables['article_info']

if __name__ == '__main__':
    pass