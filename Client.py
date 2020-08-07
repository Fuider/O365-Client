# coding=utf-8

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

from O365 import Account
from mailboxactions import MailboxActions
import os

credentials = ('74424fcf-55d7-4e15-99d7-1663c0ba2e94',)
account = Account(credentials, auth_flow_type='public')


class Start:
    """这里是应用入口"""

    def __init__(self, choice=None):
        self.choice = choice

    def mail_or_calendar(self):
        MailboxActions().check_if_authenticated()
        self.choice = input('进入邮箱还是日历？(E/C)')
        if self.choice == 'E':
            self.choice = input('看邮件还是写邮件？(R/W)')
            if self.choice == 'R':
                MailboxActions().read_email()
                self.choice = input('要阅读正文吗？（Y/N)?')
                if self.choice == 'Y':
                    print('\n')
                    MailboxActions().get_body_text()
                    os.system('pause')

            elif self.choice == 'W':
                MailboxActions().get_full_mail_info()
                MailboxActions().send_email()
            else:
                Start().mail_or_calendar()
        elif self.choice == 'C':
            print('开发中，敬请期待')
            os.system("pause")
        else:
            Start().mail_or_calendar()


start = Start()
start.mail_or_calendar()
