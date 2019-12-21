from redis import Redis
from pymysql import connect
import json

redis_cli = Redis()
conn = connect(host='本机IP地址', port=3306, user='用户', passwd='密码', db='要连接的数据库')
offset = 0
cur = conn.cursor()


def save_mysql(s, city):
    cur.execute(
        "insert into {}(location,district,house_type,lease_way,information,ancillary_facility,price,agency_fee,url) " \
        "values('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}','{}')".format(city, s['location'], s['district'],
                                                                            s['house_type'],
                                                                            s['lease_way'], s['information'],
                                                                            s['ancillary_facility'], s['price'],
                                                                            s['agency_fee'], s['url']))
    conn.commit()


while True:
    # 将数据从 redis 中 pop 出来
    source, s = redis_cli.blpop('zufang:items')
    s = json.loads(s.decode('utf-8'))
    print(s['ancillary_facility'])
    print(type(s))
    # break
    try:
        if 'bj.lianjia.com' in s['url']:
            save_mysql(s, 'bj')
        elif 'sh.lianjia.com' in s['url']:
            save_mysql(s, 'sh')
        else:
            pass
        offset += 1
        print("存储了{}".format(offset))
    except Exception as e:
        print(e)
