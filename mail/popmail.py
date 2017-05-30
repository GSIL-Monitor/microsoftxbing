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
        self.mailcount = ''
        self.inbox = []
        self.auth = ''

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
        :return:邮件数量,连接
        """
        self.auth = self.popconn()
        try:
            self.auth.user(self.user)
            self.auth.pass_(self.pw)
            ret = self.auth.stat()
            # print '共{}封邮件'.format(ret[0])
            self.mailcount = ret[0]
            return ret[0],self.auth  # 返回邮件数量和授权连接
        except Exception as e:
            print e
            raise '用户名或密码错误'

    def getmail(self, serial=None):
        """
        :param serial: 切片取邮件
        :return:
        """
        if not isinstance(serial,tuple):
            raise '参数错误,应为元组类型'
        for i in serial:
            if not isinstance(i, int):
                raise '参数错误，应为整型元组'
        if serial[1]-serial[0] != 1:
            raise '参数错误，一次只取一封邮件'
            # TODO 2.0再增加功能解析多封邮件

        if self.auth:
            mailbox = self.auth
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

        else:
            self.userauth()
            self.getmail()

    def mailmsg(self):
        # recipient = ''
        # recipient_addr = ''
        # sender = ''
        # sender_addr = ''
        # subjects = ''
        # text = ''
        # cont = '\r'.join(self.inbox[0][1]).decode('utf-8')
        cont = '\r'.join(self.inbox[0][1])
        msg = parser.Parser().parsestr(cont)
        return msg

        # TODO 收件人解析 放到另外一个方法里
        # recipient_cont = utils.parseaddr(msg.get('to'))
        # # print recipient_cont
        # recipient_addr = recipient_cont[1]
        # deName = Header.decode_header(recipient_cont[0])
        # if deName[0][1] != None:
        #     recipient = unicode(deName[0][0],deName[0][1])
        #
        # #发件人解析
        # sender_cont = utils.parseaddr(msg.get('from'))
        # # print recipient_cont
        # sender_addr = sender_cont[1]
        # deName = Header.decode_header(sender_cont[0])
        # sender = unicode(deName[0][0],deName[0][1])
        #
        # #解析标题
        # subjects_cont = utils.parseaddr(msg.get('subject'))
        # deSubjects = Header.decode_header(subjects_cont[1])
        # if deSubjects[0][1] != None:
        #     subjects = unicode(deSubjects[0][0], deSubjects[0][1])
        # # print subjects
        # return recipient,recipient_addr,sender,sender_addr,subjects


if __name__ == '__main__':
    st = MailConn(host='pop.exmail.qq.com',user='xb04@datatang.cn',pw='Zaixian2015',port=995)
    count = st.userauth()
    # print count[1]
    st.getmail(serial=(18,19))
    print st.inbox[0][1]
    # print st.dumpmail()
    # ret = st.dumpmail()
    # for i in ret:
    #     print i
    #     pass
