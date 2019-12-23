from flask import Flask,send_from_directory,\
    redirect,url_for,render_template,request,\
    Response,make_response,session,escape,send_file
                                            # 重定向
import pandas as pd
import Data_analysis as data_parse
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

@app.route('/BJ_SH_bar')
def bj_sh_bar():

    return render_template('1bj_sh_bar.html')

@app.route('/SH_bar')
def sh_bar():
    return render_template('1sh_bar.html')



# ===============================================================
# ===============================================================

# 需将此文件及数据'1bj_info.csv'   '2sh_info.csv'    放到 flask  环境中
# 再将 bar 图 与 pie  图 放到 static 中

bj_df = read_data('1bj_info.csv')
sh_df = read_data('2sh_info.csv')


@app.route('/BJ_SH_pie')
def bj_sh_pie():

    lst_price = data_parse.list_price

    return render_template('2bj_sh_pie.html', lst_price = lst_price)


@app.route('/SH_pie')
def sh_pie():

    SH_area_lst = sh_df.groupby(['district']).sum().index.to_list()
    return render_template('2sh_pie.html',SH_area_lst=SH_area_lst)


@app.route('/BJ/index/<price>')
def bj_pie_index(price):
    global dict_info,lst_info
    lst_info = []

    bj_df1 = pd.read_csv('1bj_info.csv')
    columns_lst = bj_df1.columns.to_list()
    columns_lst.remove('Unnamed: 0')
    columns_lst.remove('id')
    columns_lst.remove('district')
    columns_lst.insert(0, 'district')
    print(columns_lst)
    c,b,res = data_parse.bj_two(price)
    print(res)
    length = len(res[columns_lst[0]].to_list())
    for index in range(length):
        dict_info = {}
        for columns in columns_lst:
            dict_info[columns] = res[columns].to_list()[index]
        lst_info.append(dict_info)


    if price == '1500以下':
        img_name = 'BJ_area_price1.png'
        return render_template('3BJ_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)

    elif price == '2000-3000':
        img_name = 'BJ_area_price3.png'
        return render_template('3BJ_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)
    elif price == '1500-2000':
        img_name = 'BJ_area_price2.png'
        return render_template('3BJ_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)

    elif price == '3000-5000':
        img_name = 'BJ_area_price4.png'
        return render_template('3BJ_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)

    elif price == '5000-8000':
        img_name = 'BJ_area_price5.png'
        return render_template('3BJ_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)

    elif price == '8000以上':
        img_name = 'BJ_area_price6.png'
        return render_template('3BJ_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)




@app.route('/SH/index/<price>')
def sh_pie_index(price):
    global dict_info,lst_info
    lst_info = []
    sh_df1 = pd.read_csv('2sh_info.csv')
    columns_lst = sh_df1.columns.to_list()
    columns_lst.remove('Unnamed: 0')
    columns_lst.remove('id')
    columns_lst.remove('district')
    columns_lst.insert(0,'district')
    print(columns_lst)
    c,b,res = data_parse.sh_two(price)
    print(res)
    length = len(res[columns_lst[0]].to_list())
    for index in range(length):
        dict_info = {}
        for columns in columns_lst:
            dict_info[columns] = res[columns].to_list()[index]
        lst_info.append(dict_info)

    if price == '1500以下':
        img_name = 'SH_area_price1.png'
        return render_template('3SH_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)

    elif price == '2000-3000':
        img_name = 'SH_area_price3.png'
        return render_template('3SH_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)
    elif price == '1500-2000':
        img_name = 'SH_area_price2.png'
        return render_template('3SH_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)

    elif price == '3000-5000':
        img_name = 'SH_area_price4.png'
        return render_template('3SH_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)

    elif price == '5000-8000':
        img_name = 'SH_area_price5.png'
        return render_template('3SH_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)

    elif price == '8000以上':
        img_name = 'SH_area_price6.png'
        return render_template('3SH_index.html', lst_info=lst_info, price=price, columns_lst=columns_lst,
                               img_name=img_name)





if __name__ == '__main__':
    # app.run(debug=True,host='0.0.0.0')
    app.run(debug=True)


