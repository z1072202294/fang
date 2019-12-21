import csv
import mysql.connector
import pandas as pd

# 创建 Mysql 连接数据库
connection = mysql.connector.connect(
    user='用户',
    password='密码',
    host='本机IP地址',
    database='要连接的数据库',
    port=3306
)


# 使用 SQL 和 链接 从数据库汇总读取数据
def save_csv(city):
    data = pd.read_sql(
        "select * from {}".format(city),
        con=connection
    )

    print(data)

    data.to_csv('{}_info.csv'.format(city))


# save_csv('bj')
# save_csv('sh')
# connection.close()
res = pd.read_csv('bj_info.csv')
print(type(res))
print(res)
