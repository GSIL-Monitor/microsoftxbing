# -*- coding:utf-8 -*-
import poplib
import MySQLdb,time
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import multiprocessing
from email import *


class MailConn:

    def __init__(self,host,user,pw,port,methodConn='SSL'):
        """
        inbox：收件箱，先执行getmail，收件箱才放入邮件inbox
        """
        self.host = host
        self.user = user
        self.pw = pw
        self.port = port
        self.methodConn = methodConn
        self.handle = ''
        self.mailcount = ''
        self.inbox = []

    def popconn(self):
        if self.methodConn == 'SSL':
            try:
                conn = poplib.POP3_SSL(self.host,port=self.port)
                print("Connect to {0}:{1} successfully by SSL".format(self.host, self.port))
                # hello.set_debuglevel(1)
                return conn
            except Exception as e:
                print e
                raise '连接错误'

        if self.methodConn != 'SSL':
            try:
                conn = poplib.POP3(self.host, port=self.port)
                print("Connect to {0}:{1} successfully".format(self.host, self.port))
                # hello.set_debuglevel(1)
                return conn
            except Exception as e:
                print e
                raise '连接错误'

    def userauth(self):

        """
        用户认证
        :return:邮件数量
        """
        auth = self.popconn()
        try:
            auth.user(self.user)
            auth.pass_(self.pw)
            ret = auth.stat()
            print '共{}封邮件'.format(ret[0])
            self.mailcount = ret[0]
            self.handle = auth
            return ret[0]
        except Exception as e:
            print e
            raise '用户名或密码错误'

    def getmail(self, serial=None):
        """
        :param serial: 切片取邮件
        :return:
        """
        if self.handle:
            mailbox = self.handle
            count = self.mailcount
            if serial:
                for i in range(serial[0],serial[1]):
                    msg = mailbox.retr(i)
                    self.inbox.append(msg)
            else:
                for i in range(1,count+1):
                    # time.sleep(0.05)
                    msg = mailbox.retr(i)
                    self.inbox.append(msg)

        elif not self.handle:
            self.userauth()
            self.getmail()

    def dumpmail(self):
        recipient = ''
        recipient_addr = ''
        sender = ''
        sender_addr = ''
        subjects = ''
        text = ''
        # msg = self.inbox[0][1]
        cont = '\r'.join(self.inbox[0][1]).decode('utf-8')
        msg = parser.Parser().parsestr(cont)

        #收件人解析
        recipient_cont = utils.parseaddr(msg.get('to'))
        # print recipient_cont
        recipient_addr = recipient_cont[1]
        deName = Header.decode_header(recipient_cont[0])
        recipient = unicode(deName[0][0],deName[0][1])

        #发件人解析
        sender_cont = utils.parseaddr(msg.get('from'))
        # print recipient_cont
        sender_addr = sender_cont[1]
        deName = Header.decode_header(sender_cont[0])
        sender = unicode(deName[0][0],deName[0][1])

        #解析标题
        subjects_cont = utils.parseaddr(msg.get('subject'))
        deSubjects = Header.decode_header(subjects_cont[1])
        subjects = unicode(deSubjects[0][0], deSubjects[0][1])
        # print subjects

        return recipient,recipient_addr,sender,sender_addr,subjects

if __name__ == '__main__':
    st = MailConn(host='pop.exmail.qq.com',user='xb04@datatang.cn',pw='Zaixian2015',port=995)
    count = st.userauth()
    # print count
    st.getmail(serial=(4,5))
    ret = st.dumpmail()
    for i in ret:
        # print i
        pass
