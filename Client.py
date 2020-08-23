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
from settings import Setlang
import os


class Start:
    """这里是应用入口"""

    """The start of the app."""
    def __init__(self, choice=None):
        self.choice = choice

    def mail_or_calendar(self):
        MailboxActions().check_if_authenticated()
        self.choice = input('进入邮箱还是日历？(E/C) 您也可以向我们反馈。(S)')
        if self.choice == 'E':
            self.choice = input('Do you want to read an email (R) or write an email (W)?')
            if self.choice == 'R':
                MailboxActions().read_email()
                self.choice = input('Do you want to read the body of the email?')
                if self.choice == 'Y':
                    print('\n')
                    MailboxActions().get_body()
                    os.system('pause')
                else:
                    os.system('pause')
            elif self.choice == 'W':
                MailboxActions().get_full_mail_info()
                MailboxActions().send_email()
            else:
                Start().mail_or_calendar()
        elif self.choice == 'C':
            Read().load_events()
            Read().clear_event()

            os.system("pause")
        elif self.choice == 'S':
            Support().support()
        else:
            Start().mail_or_calendar()
            os.system("pause")


class Languagecheck:
    """这里用于检测语言"""

    def lang_chck(self):

        lang_exists = os.path.isfile("lang")
        if lang_exists == True:
            f1 = open('lang', encoding='utf-8', mode='r')
            msg = f1.read()
            if msg == '1':
                Start().mail_or_calendar()
            elif msg == '2':
                En_Start().mail_or_calendar()
        else:
            print("请设置你的语言,然后重启应用。Please set your language, then restart the program.")
            Setlang().set_language()


langu = Languagecheck()
langu.lang_chck()
