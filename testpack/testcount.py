# -*- coding: utf-8 -*-
from email.header import decode_header
from email.utils import parseaddr
from mail.popmail import *
from basefunc.strdecoding import Decode4Str
import chardet

class ParseEmail:
    """
    解析邮件
    """

    def __init__(self,msg):
        self.msg = msg
        self.sender = ''
        self.to = ''
        self.subject = ''

    def decode_str(self,s):
        """
        获取编码
        :param s:
        :return:
        """
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
        return subjects, sender, to


if __name__ == '__main__':
    st = MailConn(host='pop.exmail.qq.com',user='xb04@datatang.cn',pw='Zaixian2015',port=995)
    count = st.userauth()
    print '总邮件数:{}'.format(count[0])
    log = open('mail.log','w+')

    mailcont = 0
    for i in range(count[0],1,-1):
        if i == 0:
            break
        msg = st.mailmsg(serial=(i-1,i))
        mail = ParseEmail(msg)
        ret = mail.mailstruc()
        # print len(ret)
        for i in ret:
            try:
                if not isinstance(i, unicode):
                    i = unicode(i,'utf-8',errors='ignore')
                log.write(i + '\r')
            except Exception as e:
                log.write(str(i.encode('utf-8', 'ignore')) + '\r')
                # log.write(str(e) + '\r')
        mailcont += 1
        mails = int(count[0]) - mailcont
        log.write('======%s======\r\n' % str(mails))
        log.flush()
    log.close()

    count[1].quit()