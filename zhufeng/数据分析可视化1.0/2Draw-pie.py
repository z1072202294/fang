import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib
import numpy as np
import Data_analysis as data_parse

# def sh_pie():
#     plt.rcParams['font.sans-serif'] = ['simhei']
#     labels = data_parse.SH_area_lst
#     X = data_parse.SH_price_lst
#     plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
#     plt.title("上海各区租房房价的占比")
#     # plt.show()
#     plt.savefig('SH_pie.png')
#
# def bj_pie():
#     plt.rcParams['font.sans-serif'] = ['simhei']
#     labels = data_parse.BJ_area_lst
#     X = data_parse.BJ_price_lst
#     plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
#     plt.title("北京各区租房房价的占比")
#     plt.savefig('BJ_pie.png')

# sh_pie()
# bj_pie()


# ==================================================================




def sh_pie_num():
    plt.rcParams['font.sans-serif'] = ['simhei']
    X,labels = data_parse.sh_list_num,data_parse.list_price
    plt.pie(X,labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
    plt.title("上海租房价位数量占比 ")
    # plt.show()
    plt.savefig('static\SH_pie_num.png')



def bj_pie_num():
    explode = (0.6, 0, 0.6, 0, 0, 0)
    plt.rcParams['font.sans-serif'] = ['simhei']
    X, labels = data_parse.bj_list_num, data_parse.list_price

    plt.pie(X,explode=explode, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）

    plt.title("北京租房价位数量占比 ")
    # plt.axis('equal')  # 该行代码使饼图长宽相等
    # plt.show()
    plt.savefig('static\BJ_pie_num.png')




explode1 = (0.3, 0, 0.1, 1.2, 1.1, 0.3, 0.7, 0.8, 0.9, 1, 1.1, 1.2)
explode_bj_1 = (0,0,0.2,0,0)
explode2 = (0,0.2,0,0.3,0,0,0,0,0)
explode_bj_2 = (0,0.2,0,0,0,0)

explode3 = (0.2,0,0.2,1.2,0,1.2,0.95,0,0,0,0,0,0.2,0)
explode_bj_3 = (0.4,0,0.4,0.2,0,0.2,0,1,0,0.8,0.8,0,0)
explode4 = (0,0,0,0,0,0,0,0.2,0.6,0.2,0.6,0,0,0,0)
explode_bj_4 = (0,0,0,0,0,0,0,0,0.4,0,0.2,0,0)

explode5 = (0,0,0,0,0,0,0,0,0.2,0.2,0.4,0.2,0,0,0,0)
explode_bj_5 = (0,0,0,0,0,0.2,0,0,0,0.2,0)

explode6 = (0,0.6,0,0.2,0,0,0.2,0.6,0,0.6,0,0.4,0,0.2,0)

explode_bj_6 = (0,0,0.2,0.6,0.4,0.2,0,0.2,0,0.2,0,0,0)



def city_area_pie(city,str_price):
    if city == '上海':
        plt.figure(figsize=(7, 6.5))
        plt.rcParams['font.sans-serif'] = ['simhei']
        X, labels = data_parse.sh_two(str_price)
        print(X)
        print(labels)
        print(len(X))
        plt.pie(X,explode=explode6,labels=labels, autopct='%1.2f%%',textprops={'fontsize':10,'color':'black'})  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
        plt.title("上海租房{}价位各区数量占比".format(str_price))
        plt.legend(loc="upper left", fontsize=10, bbox_to_anchor=(1.05, 1.1), borderaxespad=1,ncol=2)
        # plt.show()
        plt.savefig('static\SH_area_price6.png',dpi=200,bbox_inches='tight')

    elif city == '北京':
        plt.figure(figsize=(10, 6.5))
        plt.rcParams['font.sans-serif'] = ['simhei']
        X, labels = data_parse.bj_two(str_price)
        print(X)
        print(labels)
        print(len(X))
        plt.pie(X,explode=explode_bj_6,labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
        plt.title("北京租房{}价位各区数量占比 ".format(str_price))
        plt.legend(loc="upper left", fontsize=10, bbox_to_anchor=(1.2, 1.2), borderaxespad=1, ncol=1)
        # plt.show()
        # plt.savefig('static\BJ_area_price6.png',dpi=200,bbox_inches='tight')

# sh_pie_num()
# bj_pie_num()

# city_area_pie('上海','1500下')
# city_area_pie('北京','1500下')

# city_area_pie('上海','1500-2000')
# city_area_pie('北京','1500-2000')
#
# city_area_pie('上海','2000-3000')
# city_area_pie('北京','2000-3000')
#
# city_area_pie('上海','3000-5000')
# city_area_pie('北京','3000-5000')
#
# city_area_pie('上海','5000-8000')
# city_area_pie('北京','5000-8000')
#
city_area_pie('上海','8000上')
# city_area_pie('北京','8000上')
















# ========================================================================

# 设置中文字体和负号正常显示
# kaiti_font_path =  r"C:\Windows\Fonts\simkai.ttf"
# my_font = font_manager.FontProperties(fname=kaiti_font_path)
# plt.title('北京城市各区租房 (-Price-)统计表',fontproperties = my_font)


# ==========================================================================
# ==========================================================================



# plt.figure(figsize=(10,6),dpi=80)   # 设置图像大小，主要参数为figsize(a,b)
# lst_x = [0,1,2,3,4]
# lstx = ['延庆区','昌平区','朝阳区','海淀区','东城区','西城区','丰台区','石景山区']
#
# lst_y = [1000,1600,2500,4600,4700,3600,4400,5050]
# plt.bar(lst_x,lst_y)
# # plt.xticks(lst_x,lstx)
# # plt.show()


# =========================================
# =========================================


