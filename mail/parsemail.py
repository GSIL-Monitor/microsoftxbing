# -*- coding:utf-8 -*-
from email.header import decode_header
from email.utils import parseaddr
from popmail import MailConn
from email import parser
from popmail import *


class ParseEmail:

    def __init__(self,msg):
        self.msg = msg
        self.sender = ''
        self.to = ''
        self.subject = ''

    def decode_str(self,s):
        value, charset = decode_header(s)[0]
        if charset:
            value = value.decode(charset)
        return value

    def mailstruc(self):
        sender = ''
        subjects = ''
        to = ''
        for header in ['From','Subject','To']:
            value = self.msg.get(header, '')
            # print value
            if value:
                if header == 'Subject':
                    value = self.decode_str(value)
                    subjects = ''.join(value)
                    # print subjects
                elif header == 'From':
                    hdr, addr = parseaddr(value)
                    name = self.decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
                    sender = value
                    # print sender
                elif header == 'To':
                    hdr, addr = parseaddr(value)
                    name = self.decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
                    to = value
                    # print to
        return subjects,sender,to
        # return sender,subjects
            # print('%s: %s' % (header, value))





st = MailConn(host='pop.exmail.qq.com',user='xb04@datatang.cn',pw='Zaixian2015',port=995)
count = st.userauth()
print '总邮件数:{}'.format(count[0])
st.getmail(serial=(917,918))
msg = st.mailmsg()
# msg = st.inbox[0][1]
# cont = '\r'.join(msg)
# message = parser.Parser().parsestr(cont)
# print message
mail = ParseEmail(msg)
ret = mail.mailstruc()
for i in ret:
    print i