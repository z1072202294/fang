import json
from pymysql import connect

s = {"location": "\u5bcc\u83b1\u8335\u82b1\u56ed", "district": "\u4e1c\u57ce", "house_type": "2\u5ba41\u5385",
     "lease_way": "\u6574\u79df",
     "information": "\u9762\u79ef\uff1a70\u33a1 \u671d\u5411\uff1a\u4e1c  \u7ef4\u62a4\uff1a\u4eca\u5929 \u5165\u4f4f\uff1a2019-12-30  \u697c\u5c42\uff1a\u4e2d\u697c\u5c42/21\u5c42 \u7535\u68af\uff1a\u6709  \u8f66\u4f4d\uff1a\u6682\u65e0\u6570\u636e \u7528\u6c34\uff1a\u6c11\u6c34  \u7528\u7535\uff1a\u6c11\u7535 \u71c3\u6c14\uff1a\u6709  \u91c7\u6696\uff1a\u96c6\u4e2d\u4f9b\u6696 \u79df\u671f\uff1a3\u5e74\u4ee5\u4e0a   \u770b\u623f\uff1a\u9700\u63d0\u524d\u9884\u7ea6   ",
     "ancillary_facility": [], "price": "5800", "agency_fee": "5800",
     "url": "https://bj.lianjia.com/zufang/BJ2412073585377558528.html"}
a = {"location": "\u6c38\u534e\u5317\u91cc", "district": "\u5927\u5174", "house_type": "2\u5ba41\u5385",
     "lease_way": "\u6574\u79df",
     "information": "\u9762\u79ef\uff1a75\u33a1 \u671d\u5411\uff1a\u5357 \u5317  \u7ef4\u62a4\uff1a3\u5929\u524d \u5165\u4f4f\uff1a\u968f\u65f6\u5165\u4f4f  \u697c\u5c42\uff1a\u9ad8\u697c\u5c42/6\u5c42 \u7535\u68af\uff1a\u65e0  \u8f66\u4f4d\uff1a\u6682\u65e0\u6570\u636e \u7528\u6c34\uff1a\u6c11\u6c34  \u7528\u7535\uff1a\u6c11\u7535 \u71c3\u6c14\uff1a\u6709  \u91c7\u6696\uff1a\u96c6\u4e2d\u4f9b\u6696 \u79df\u671f\uff1a\u6682\u65e0\u6570\u636e   \u770b\u623f\uff1a\u9700\u63d0\u524d\u9884\u7ea6   ",
     "ancillary_facility": ["\n                ", "\n                \u7535\u89c6              ", "\n                ",
                            "\n                \u51b0\u7bb1              ", "\n                ",
                            "\n                \u6d17\u8863\u673a              ", "\n                ",
                            "\n                \u7a7a\u8c03              ", "\n                ",
                            "\n                \u70ed\u6c34\u5668              ", "\n                ",
                            "\n                \u5e8a              ", "\n                ",
                            "\n                \u6696\u6c14              ", "\n                ",
                            "\n                \u5bbd\u5e26              ", "\n                ",
                            "\n                \u8863\u67dc              ", "\n                ",
                            "\n                \u5929\u7136\u6c14              "], "price": "3500",
     "agency_fee": "3500", "url": "https://bj.lianjia.com/zufang/BJ2326060252744916992.html"}
print(type(s))
# print(json.loads(s['location']))
print(a['ancillary_facility'])
