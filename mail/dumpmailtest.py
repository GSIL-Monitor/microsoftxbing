# -*- coding:utf-8 -*-
from email import *
from popmail import MailConn
import sys
reload(sys)
sys.setdefaultencoding('gbk')
from email.mime.text import MIMEText

st = MailConn(host='pop.exmail.qq.com',user='xb04@datatang.cn',pw='Zaixian2015',port=995)
count = st.userauth()
# print count
st.getmail(serial=(2,3))
list1 = st.inbox
messages = list1[0][1]
cont = '\r'.join(messages).decode('utf-8')
msg = parser.Parser().parsestr(cont)
# print utils.parseaddr(msg.get("from"))
# print msg.get("from")
print MIMEText(_text=msg.get("from")[1],_charset='gb18030')

deCont = Header.decode_header(msg.get('subject'))[0]
for part in msg.walk():
    # print 'cont:{}'.format(part.get_payload(decode=True))
    pass