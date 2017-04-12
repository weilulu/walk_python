#!/usr/bin/python
# _*_ coding: UTF-8 _*_
from sqlalchemy import create_engine,MetaData
from sqlalchemy import Table,Column
from sqlalchemy import Integer,String,TIMESTAMP
dbr = create_engine("mysql://root:root@127.0.0.1:3306/walk-management",pool_size=50,max_overflow=100,echo=True,pool_timeout=10)

metaRead = MetaData()
metaRead.reflect(bind=dbr)
metaRead.bind = dbr

def getTable():
    pass
