import numpy as np
import matplotlib.pyplot as plt
import matplotlib,random
from matplotlib import font_manager
import Data_analysis as data_parse
import seaborn as sns

def SH_img_histogram():
    sns.set(style='white', font_scale=1.2)
    # 保证可以显示中文字体
    plt.rcParams['font.sans-serif'] = 'simhei'
    # 设置字体大小
    font1 = {'family': 'simhei',
             'weight': 'normal',
             'size': 20, }
    f, ax = plt.subplots(figsize=(12, 6))
    # 画柱形图
    region_pivot =  data_parse.SH_price_pivot
    bar = plt.bar(region_pivot['district'].values, region_pivot['price'].values, color='dodgerblue')
    bar[0].set_color('red')
    print(region_pivot['price'].values)
    # print('=========================================')
    for x, y in enumerate(region_pivot['price'].values):
        print(x)
        print(y)
        plt.text(x - 0.4, y + 500, "%s" % y)
    # 删除所有边框
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set(title='上海各区域二手房总价', xlabel='地区', ylabel='总价')
    plt.tick_params(labelsize=14)
    plt.xlabel('地区', font1)
    plt.xticks(region_pivot['district'].values)
    plt.ylabel('平均价格', font1)
    plt.title('上海各区域租房平均价格', font1)
    plt.show()
    # f.savefig('static\SH_bar.png', bbox_inches='tight')



def BJ_img_histogram():
    sns.set(style='white', font_scale=1.2)
    # 保证可以显示中文字体
    plt.rcParams['font.sans-serif'] = 'simhei'
    # 设置字体大小
    font1 = {'family': 'simhei',
             'weight': 'normal',
             'size': 18, }
    f, ax = plt.subplots(figsize=(12, 6))
    # 画柱形图
    region_pivot =  data_parse.BJ_price_pivot
    bar = plt.bar(region_pivot['district'].values, region_pivot['price'].values, color='dodgerblue')
    bar[0].set_color('red')
    print(region_pivot['price'].values)
    # print('=========================================')
    for x, y in enumerate(region_pivot['price'].values):
        print(x)
        print(y)
        plt.text(x - 0.4, y + 500, "%s" % y)
    # 删除所有边框
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set(title='北京各区域二手房总价', xlabel='地区', ylabel='总价')
    plt.tick_params(labelsize=14)
    plt.xlabel('地区', font1)
    plt.xticks(region_pivot['district'].values)
    plt.ylabel('平均价格', font1)
    plt.title('北京各区域租房平均价格', font1)
    plt.show()
    # f.savefig('static\BJ_bar.png', bbox_inches='tight')

SH_img_histogram()
BJ_img_histogram()






















# kaiti_font_path =  r"C:\Windows\Fonts\simkai.ttf"
# my_font = font_manager.FontProperties(fname=kaiti_font_path)
# plt.title('北京城市各区租房 (-Price-)统计表',fontproperties = my_font)


# def SH_img_histogram():
#     # plt.figure(figsize=(30,10))
#     X_city = data_parse.SH_area_lst
#     X_num = np.arange(0, len(X_city) * 2, 2)  # X决定了各个bar在X轴的位置
#     height = data_parse.SH_price_lst  # height决定了各个bar的高度
#     plt.tick_params(labelsize=14)
#     plt.bar(X_num,height)                                    #X,height为必须参数
#     plt.xticks(X_num,X_city,fontproperties = my_font)
#     plt.xlabel('城市',fontproperties = my_font)
#     plt.ylabel('价格',fontproperties = my_font)
#     # plt.savefig('SH_historgram.png')
#
#
#     plt.show()

    # plt.imsave('SH_historgram.png')


# =================================================================
#                     条形图

# lst_x = ['延庆','昌平','朝阳','海淀']
# print(range(20))
# print(type(range(20)))





# plt.figure(figsize=(20,8))
# x = range(1000,15000)
#
# random.seed(100)   # 设置随机种子 , 让不同时候随机的得到的结果都一样
# # y = [random.uniform(20,35) for i in range(120)]
# # print(y)
#
# # print(random.uniform(20,35))
# y = [random.uniform(1000,15000) for i in range(0,20000,1500)]
# print(y)
#
# plt.plot(x,y)
#
# _x_ticks = ["10点{}分".format(i) for i in x if i < 60]
# _x_ticks += ["11点{}分".format(i-60) for i in x if i > 60]
#
# print(_x_ticks)
        #  --->  设置 x 轴上的字符串的可读


# plt.xticks(x[::5],_x_ticks[::5],fontproperties = my_font)
# plt.xlabel('城市',fontproperties = my_font)
# # plt.xlim(right=range(1000,20000,1500))
#
# plt.ylabel('价格',fontproperties = my_font,)rotation=45
# plt.show()



# ==============================================================================
# ==============================================================================


# for i in range(1000,20000,1500):
#     print(i)
#  =============================================

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C,S = np.cos(X), np.sin(X)
#
# plt.plot(X,C)
# plt.plot(X,S)
#
# plt.show()