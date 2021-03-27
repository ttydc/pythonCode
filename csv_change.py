import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy as sqla


path = r'D:\study\python_study\practice\python_sql\province_gdp.csv'
data = pd.read_csv(path,encoding='gbk') # 读取成pd数组

# 把数组转化成包含多个元组的list，方便插入sql
sqldata=[]
for i in range(data.index.max()):
    frame = []
    for j in data.columns:
        frame.append(data.loc[i,j])
    sqldata.append(tuple(frame))

print(sqldata)


# 以下是将python连接到sql的做法

drop="drop table 'province'" # 删除表
con.execute(drop)

query = "CREATE TABLE province (a VARCHAR(50), b int);" #创建表
con = sqlite3.connect('mydata.sqlite')
con.execute(query)
con.commit()

stmt = "INSERT INTO province VALUES(?,?)" # 插入数据
con.executemany(stmt, sqldata)
con.commit()

db = sqla.create_engine('sqlite:///mydata.sqlite') # 读取sql模式下的数据
pd.read_sql('select * from province', db)



