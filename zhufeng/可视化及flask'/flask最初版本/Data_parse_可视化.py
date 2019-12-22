from flask import Flask,send_from_directory,\
    redirect,url_for,render_template,request,\
    Response,make_response,session,escape,send_file
                                            # 重定向
import pandas as pd

# 分析 csv 中的 data

def read_data(file_name):
    # df = pd.read_csv(file_name,index_col='id')
    df = pd.read_csv(file_name,index_col='id')
    return df

# bj_df = read_data('1bj_info.csv')
# sh_df = read_data('2sh_info.csv')

# BJ_area_lst = bj_df.groupby(['district']).sum().index.to_list()
# SH_area_lst = sh_df.groupby(['district']).sum().index.to_list()

# ['东城', '丰台', '亦庄开发区', '大兴', '平谷', '房山', '昌平', '朝阳', '海淀', '石景山', '西城', '通州', '顺义']
# ['嘉定', '奉贤', '宝山', '崇明', '徐汇', '普陀', '杨浦', '浦东', '虹口', '闵行', '青浦', '静安', '黄浦']




app = Flask(__name__)

@app.route('/BJ_bar')
def bj_bar():

    return render_template('1bj_bar.html')

@app.route('/SH_bar')
def sh_bar():
    return render_template('1sh_bar.html')



# ===============================================================
# ===============================================================

# 需将此文件及数据'1bj_info.csv'   '2sh_info.csv'    放到 flask  环境中
# 再将 bar 图 与 pie  图 放到 static 中

bj_df = read_data('1bj_info.csv')
sh_df = read_data('2sh_info.csv')


@app.route('/BJ_pie')
def bj_pie():

    BJ_area_lst = bj_df.groupby(['district']).sum().index.to_list()
    return render_template('2bj_pie.html',BJ_area_lst=BJ_area_lst)

@app.route('/SH_pie')
def sh_pie():

    SH_area_lst = sh_df.groupby(['district']).sum().index.to_list()
    return render_template('2sh_pie.html',SH_area_lst=SH_area_lst)


@app.route('/BJ/index/<area>')
def bj_pie_index(area):
    global dict_info,lst_info
    lst_info = []
    columns_lst = bj_df.columns.to_list()
    columns_lst.remove('Unnamed: 0')
    columns_lst.remove('district')
    a = bj_df[bj_df['district'] == area]
    length = len(a[columns_lst[0]].to_list())
    for index in range(length):
        dict_info = {}
        for columns in columns_lst:
            dict_info[columns] = a[columns].to_list()[index]
        lst_info.append(dict_info)
    return render_template('3BJ_index.html', lst_info = lst_info,area=area,columns_lst = columns_lst)

@app.route('/SH/index/<area>')
def sh_pie_index(area):
    global dict_info,lst_info
    lst_info = []
    print(sh_df)
    columns_lst = sh_df.columns.to_list()
    columns_lst.remove('Unnamed: 0')
    columns_lst.remove('district')
    a = sh_df[sh_df['district'] == area]
    length = len(a[columns_lst[0]].to_list())
    for index in range(length):
        dict_info = {}
        for columns in columns_lst:
            dict_info[columns] = a[columns].to_list()[index]
        lst_info.append(dict_info)


    return render_template('3SH_index.html',lst_info = lst_info,area = area,columns_lst = columns_lst)


if __name__ == '__main__':
    app.run(debug=True)


