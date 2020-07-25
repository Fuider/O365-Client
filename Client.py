# coding=utf-8
from O365 import Account
import os

credentials = ('74424fcf-55d7-4e15-99d7-1663c0ba2e94',)
account = Account(credentials, auth_flow_type='public')


class mailbox_actions:
    """用来对邮箱进行操作"""

    def __init__(self, choice=None):

        # 这是我的应用ID和机密，但是公共客户端流还是没有实现，文档里说下面改为
        # self.account = Account(self.credentials, auth_flow_type=‘pubic')
        # （上面是我的理解）就行了但他报错
        self.account = account
        self.credentials = credentials
        self.choice = choice
        self.scopes = ['basic', 'message_all']  # 请求权限

    def check_if_authenticated(self):
        """检查是否有用户登录，若无，则请求登录"""
        if not self.account.is_authenticated:  # 检查是否登录
            # 请求登录
            self.account.authenticate(scopes=self.scopes)

    def read_email(self):
        """遍历邮件
        limit 表示加载多少个，微软官方一次API调用只返回999个，
        而O365模块默认25个，只有limit>25时utils分页功能才生效
        batch批处理表示加载多少次，就是往后加载
        limit=2000, batch=10 = limit=2000
        但是分为10次加载。"""

        mailbox = self.account.mailbox()
        print('''
        你要进入哪个文件夹？
        1.收件箱
        2.已发送
        3.垃圾邮件
        4.已删除\n
        ''') # 选择进入哪个文件夹
        readbox = input('请输入对应数字')

        if readbox == '1':
            readbox = mailbox.inbox_folder()
        elif readbox == '2':
            readbox = mailbox.sent_folder()
        elif readbox == '3':
            readbox = mailbox.junk_folder()
        else:
            readbox = mailbox.deleted_folder()

        for messages in readbox.get_messages(limit=2000, batch=100):  # 下面的都是utils分页的
            print(messages)

        os.system("pause")

    def send_email(self):
        email_will_send=mailbox.ne


class Start:
    """这里是应用入口"""
    def __init__(self):
        pass

    def mail_or_calendar(self):
        self.choice = input('进入邮箱还是日历？(E/C)')
        if self.choice == 'E':
            self.choice = input('看邮件还是写邮件？(R/W)')
            if self.choice == 'R':
                mailbox_actions().read_email()
            elif self.choice == 'W':
                print('开发中，请稍后')
                os.system("pause")
            else:
                Start().mail_or_calendar()
        elif self.choice == 'C':
            print('开发中，敬请期待')
            os.system("pause")
        else:
            Start().mail_or_calendar()


start = Start()
start.mail_or_calendar()
