#  O365-Client -- A client to connect O365
#  Copyright (C) 2020  Micraow
#
#  This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


# This file is translated by Xiaocao162020, there maybe mistakes, we are glad if you can tell us about the problems.


from O365 import Account
import os
import re

credentials = ('e089ce98-73af-46f6-8312-0501536effcb', )
account = Account(credentials, auth_flow_type='public')


class MailboxActions:
    """用来对邮箱进行操作"""

    """The actions in mailbox"""
    def __init__(self):

        self.account = account
        self.credentials = credentials
        self.scopes = ['basic', 'message_all', 'calendar_all']  # 请求权限

    def check_if_authenticated(self):
        """check if the user had logged in to their Microsoft account, if not, login."""
        if not self.account.is_authenticated:  # check if logged in
            # request to login
            self.account.authenticate(scopes=self.scopes)

    def read_email(self):
        

        mailbox = self.account.mailbox()
        global readbox
        print('''
        Which email folder do you want to get into?
        1.Inbox
        2.Sent emails
        3.Spam folder
        4.Deleted emails\n
        ''')  # choose which mailbox to get into
        readbox = input('Please enter the number.')

        if readbox == '1':
            readbox = mailbox.inbox_folder()
        elif readbox == '2':
            readbox = mailbox.sent_folder()
        elif readbox == '3':
            readbox = mailbox.junk_folder()
        else:
            readbox = mailbox.deleted_folder()
        for messages in readbox.get_messages(limit=75, batch=20):
            print(messages)
        os.system('pause')

    def get_body(self):
        """获取邮件正文，通过----------分割同主题的不同邮件，但是现在获取HTML邮件正文会打印源码"""
        global readbox
        will_read_sub = input('请输入要阅读的邮件的主题。\n')
        for messages in readbox.get_messages(limit=75, batch=20):
            if messages.subject == will_read_sub:
                print(messages.subject)
                print('\n----------------------------\n')
                print(messages.body)

    def send_email(self):
        """send the email with the function 'get_full_mail_info' """
        global to_who
        global subj
        global text
        m = account.new_message()
        m.to.add(to_who)
        m.subject = subj
        m.body = text
        m.send()
        print('\nEmail successfully sent. \n')
        os.system('pause')

    def get_full_mail_info(self):
        """Get the information when user requests to send an email"""
        global to_who
        global subj
        global text
        new_people = input('\nPlease enter the email address you want to send to, divide them in ";": \n')
        result1 = re.split(r'[;]', new_people)  # By @xiaocao162020
        print('Check these email addresses, press enter to continue.')
        print(result1)
        os.system('pause')
        to_who = result1
        subj = input('\nPlease enter the subject: \n')
        text = input('\nPlease enter the body: \n')
