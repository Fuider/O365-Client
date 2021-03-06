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


# This file is translated by Xiaocao162020, there maybe mistakes, we are glad if you can tell us about the problems.

from mailboxactions import MailboxActions
from events import Read
from enlib.enClient import En_Start
from support import Support
from jsonsettings import *
import json
import os

mail = MailboxActions()
calendar = Read()
sets = settings()

class Start:
    """这里是应用入口"""

    """The start of the app."""
    def __init__(self, choice=None):
        self.choice = choice

    def mail_or_calendar(self):
        mail.check_if_authenticated()
        self.choice = input('进入邮箱还是日历？(E/C) 您也可以向我们反馈。(S)或进入设置(O)')
        if self.choice == 'E':
            self.choice = input('读邮件(R)还是写邮件(W)?')
            if self.choice == 'R':
                mail.read_email()
                self.choice = input('要读正文吗?(Y/N)')
                if self.choice == 'Y':
                    print('\n')
                    mail.get_body()
                    os.system('pause')
                else:
                    os.system('pause')
            elif self.choice == 'W':
                mail.get_full_mail_info()
                mail.send_email()
            else:
                Start().mail_or_calendar()
        elif self.choice == 'C':
            calendar.load_events()
            calendar.clear_event()

            os.system("pause")
        elif self.choice == 'S':
            Support().support()
        elif self.choice == 'O':
            sets.choose_set()
        else:
            Start().mail_or_calendar()
            os.system("pause")


class Languagecheck:
    """这里用于检测语言"""
    def lang_chck(self):
        if os.path.isfile('settings.json') == True:

            settings = open('settings.json',encoding='utf-8',mode='r')
            settings_dic = json.load(settings)
            lang = settings_dic['lang']
            if sets.lang != 'Chinese':
                En_Start().mail_or_calendar()
            else:
                Start().mail_or_calendar()
        else:
            print('请前往jsonsettings.py设定你的语言，然后重启本程序。Please go to jsonsettings.py to set your language, and then go back here to restart the program.')

langu = Languagecheck()
langu.lang_chck()
