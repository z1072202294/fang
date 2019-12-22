import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib
import numpy as np
import Data_analysis as data_parse

def sh_pie():
    plt.rcParams['font.sans-serif'] = ['simhei']
    labels = data_parse.SH_area_lst
    X = data_parse.SH_price_lst
    plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
    plt.title("上海各区租房房价的占比")
    # plt.show()
    plt.savefig('SH_pie.png')

def bj_pie():
    plt.rcParams['font.sans-serif'] = ['simhei']
    labels = data_parse.BJ_area_lst
    X = data_parse.BJ_price_lst
    plt.pie(X, labels=labels, autopct='%1.2f%%')  # 画饼图（数据，数据对应的标签，百分数保留两位小数点）
    plt.title("北京各区租房房价的占比")
    plt.savefig('BJ_pie.png')

sh_pie()
# bj_pie()













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


