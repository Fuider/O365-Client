# coding=utf-8

#  O365-Client -- A client to connect O365
#  Copyright (C) 2020  Ella & Xiaocao162020
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

from mailboxactions import MailboxActions
from O365 import Account
import os

credentials = ('74424fcf-55d7-4e15-99d7-1663c0ba2e94', )
account = Account(credentials, auth_flow_type='public')

class EnSupport:
    def __init__(self, choice=None):
        self.choice = choice
    
    def support(self):
        MailboxActions().check_if_authenticated()
        """通过从获取的信息发件"""
        global to_who
        global subj
        global text
        """获取需要帮助的主题，正文，并确认"""
        subj_entered = input('\nPlease enter a main problem you have met:\n')
        subj = 'From Program: '+subj_entered
        text = input('\nPlease give us more information about it:\n')
        m = account.new_message()
        m.to.add('pengbo@pengbo0708.onmicrosoft.com')
        m.to.add('xiaocao162020@xiaocao.onmicrosoft.com')
        m.to.add('ella_1102@xiaocao.onmicrosoft.com')
        m.subject = subj
        m.body = text
        m.send()
        print('\nYour request have been sent. We will handle it as quick as we can. Please check your inbox in 3 days. Thanks!\n')
        os.system('pause')

