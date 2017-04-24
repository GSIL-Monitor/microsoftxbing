# -*- coding:utf-8 -*-
from email import *
import StringIO
from popmail import *


st = MailConn(host='pop.exmail.qq.com',user='xb04@datatang.cn',pw='Zaixian2015',port=995)
count = st.userauth()
# print count
st.getmail(serial=(2,3))
list1 = st.inbox
messages = list1[0][1]
cont = '\r'.join(messages)
msg = parser.Parser().parsestr(cont)
# print msg.walk()
print  msg.get("subject")