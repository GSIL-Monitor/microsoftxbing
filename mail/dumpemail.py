# -*- coding:utf-8 -*-
from email import *
import StringIO
from popmail import MailConn
import sys
reload(sys)
sys.setdefaultencoding('gbk')


class DumpMail:

    def __init__(self):
        pass

    def dump(self):
        pass



st = MailConn(host='pop.exmail.qq.com',user='xb04@datatang.cn',pw='Zaixian2015',port=995)
count = st.userauth()
# print count
st.getmail(serial=(2,3))
list1 = st.inbox
messages = list1[0][1]
cont = '\r'.join(messages)
msg = parser.Parser().parsestr(cont)
for i in msg.walk():
    if not i.is_multipart():
        contenttype = i.get_content_type()
        filename = i.get_filename()
        if filename:
            h = Header.Header(filename)
            dh = Header.decode_header(h)
            fname = dh[0][0]
            encodeStr = dh[0][1]
            if encodeStr != None:
                if charset == None:
                    fname = fname.decode(encodeStr, 'gbk')
                else:
                    fname = fname.decode(encodeStr, charset)
            data = i.get_payload(decode=True)
            print('Attachment : ' + fname)
            if fname != None or fname != '':
                pass #保存附件 data
        else:
            if contenttype in ['text/plain']:
                suffix = '.txt'
            if contenttype in ['text/html']:
                suffix = '.htm'
            if charset == None:
                mailContent = i.get_payload(decode=True)
            else:
                mailContent = i.get_payload(decode=True)
print (mailContent, suffix)
# print msg.get("To")
# print msg.get('from')