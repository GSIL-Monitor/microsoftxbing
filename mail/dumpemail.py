# -*- coding:utf-8 -*-
from email import *
import re
import StringIO
from popmail import MailConn
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class DumpMail:

    def __init__(self,):
        pass

    def dump(self):
        pass



st = MailConn(host='pop.exmail.qq.com',user='xb04@datatang.cn',pw='Zaixian2015',port=995)
count = st.userauth()
# print count
st.getmail(serial=(4,5))
list1 = st.inbox
messages = list1[0][1]
cont = '\r'.join(messages).decode('utf-8')
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
            # print('Attachment : ' + fname)
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

# print  'body:{}'.format(msg.get('body'))
content_type = msg.get('Content-Type', '').lower()
subjects_cont = utils.parseaddr(msg.get('subject'))
deSubjects = Header.decode_header(subjects_cont[1])
if deSubjects[0][1] != None:
    subjects = unicode(deSubjects[0][0], deSubjects[0][1])
    # print subjects
# pos = content_type.find()
# print pos

# subject = msg.get('text')
# print subject
# print 'charset:{}'.format(pos.group())
for part in msg.walk():
    # print 'info:{}'.format(part)
    # print re.findall(r'charset="([^"]+)"',part)
    pass
msginfo = msg.walk()
for part in msginfo:
    if part.is_multipart():
        'part:{}'.format(part)

    else:
        # print 'nopart:{}'.format(part)
        pass


for i in msginfo:
    pass
    mailtype = i.get_content_type() #获取正文类型
    # print mailtype
    if 'text/plain' in mailtype:
        print 'text'
        print i.get_payload(decode=True)
    elif 'text/html' in mailtype:
        print 'html'
        print i.get_payload(decode=True).decode('gb18030')


    # # message = i.get_payload()


# TODO 确定邮件正文编码是TEXT 还是HTML，然后再解析
# TODO 通过walk方法获取多个收件人
