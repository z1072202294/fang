import numpy as np
from functools import reduce
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import  Sql_message as sq_mesg
import math


# 分析 csv 中的 data

def read_data(file_name):
    # df = pd.read_csv(file_name,index_col='id')
    df = pd.read_csv(file_name,index_col='id')
    return df


bj_df = read_data('1bj_info.csv')
sh_df = read_data('2sh_info.csv')




# ===========   Area index    =======================

SH_area_lst = sh_df.groupby(['district']).sum().index.to_list()
# print(SH_area_lst)





columns_lst = sh_df.columns.to_list()
columns_lst.remove('Unnamed: 0')
# print(columns_lst)
dict_all_info = {}
lst_info = []
dict_info = {}

# a = sh_df[sh_df['district'] == '嘉定']
# print(a['url'].to_list())

# a = sh_df[sh_df['district']=='嘉定']
# print(a)


a = sh_df[sh_df['district'] == '嘉定']
length = len(a[columns_lst[0]].to_list())
# for columns in columns_lst:
for index in range(length):
    for columns in columns_lst:
        dict_info[columns] = a[columns].to_list()[index]
    lst_info.append(dict_info)
    print(lst_info)
    break







# ===========   直方图      =======================
    # 数据透视表
SH_price_pivot = round(pd.pivot_table(sh_df,values='price',index='district').reset_index().sort_values(ascending=False,by='price'),1)
BJ_price_pivot = round(pd.pivot_table(bj_df,values='price',index='district').reset_index().sort_values(ascending=False,by='price'),1)

# print(SH_price_pivot)
# print(BJ_price_pivot)

# ===========   饼图      =======================


    #  上海
SH_price_lst = sh_df.groupby(['district']).sum()['price'].to_list()
SH_area_lst = sh_df.groupby(['district']).sum().index.to_list()


# print(sh_df.groupby(['district']).sum())
# print(SH_price_lst)
# print(SH_area_lst)

#     # 北京
BJ_price_lst = bj_df.groupby(['district']).sum()['price'].to_list()
BJ_area_lst = bj_df.groupby(['district']).sum().index.to_list()








# SH_price_lst = sorted(sh_df.groupby(['district']).mean().round(1)['price'].to_list(),reverse=True)
# SH_area_lst = sh_df.groupby(['district']).mean().round(1).index.to_list()

# print('SH_area_lst',len(SH_area_lst))

    # 数据透视表
# s = round(pd.pivot_table(sh_df,values='price',index='district').reset_index().sort_values(ascending=False,by='price'),1)
# print(s)

# print(bj_df)
# print(sh_df)
# print(sh_df.columns)

# Index(['id', 'location', 'district', 'house_type', 'lease_way', 'information',
#        'ancillary_facility', 'price', 'agency_fee', 'url'],
#       dtype='object')

# BJ_url_lst = bj_df['url'].to_list()
#
# BJ_price_lst = bj_df['price'].to_list()
#
# BJ_price_mean = bj_df['price'].mean()
# BJ_district_list = bj_df['district']





# print(sum(price_list)/len(price_list))
# print(math.fmod())
# print(bj_df['district'])



    # 准备

# =================================
# =================================

# DataFrame.axes	返回一个表示DataFrame轴的列表。
# DataFrame.ndim	返回一个表示轴数/数组维数的整数。
# DataFrame.size	返回一个int表示此对象中元素的数量。
# DataFrame.shape	返回一个表示DataFrame维数的元组。
# DataFrame.memory_usage（self [，index，deep]）	返回每列的内存使用情况（以字节为单位）。
# DataFrame.empty	指示DataFrame是否为空。
# DataFrame.is_copy	返回副本。

# print(bj_df.size)
# print(bj_df.shape)
# print(bj_df.xs)
# print(bj_df.groupby(['district']).mean().round(1))
# print((bj_df.groupby(['district']).mean()))
# print(bj_df.groupby(['district'])['price'])




# =================================
# =================================


#     创建 Mysql 连接数据库
# connection = mysql.connector.connect(
#     user='root',
#     password = '222677',
#     host = '127.0.0.1',
#     database = 'pythonclass',
#     port = 3306
# )

# 使用 SQL 和 链接 从数据库汇总读取数据
# data = pd.read_sql(
#     sq_mesg.select_all_info(),
#     # sq_mesg.select_file_mesg('s_name','s_sex'),
#     # sq_mesg.select_file_condition_msg('s_name','s_sex',condition='where s_sex = "男"'),
#     con = connection
# )
# print(data.head())
# print(data.shape)
# print(data.columns)
# print(data.info())
# print(data.describe(include=['object','bool']))
#
# connection.close()


# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
#        ylabel='Y-Axis', xlabel='X-Axis')
# # plt.show()
# lst_1 = {'北京':{'延庆':[2600,8500,9500,7500]}}













