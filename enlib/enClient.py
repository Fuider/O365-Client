# coding=utf-8

#  O365-Client -- A client to connect O365
#  Copyright (C) 2020  Micraow, Ella, Xiaocao
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

from .enMailboxactions import MailboxActions
from events import Read
from .enSupport import EnSupport
import os


class En_Start:
    """The start of the app."""

    def __init__(self, choice=None):
        self.choice = choice

    def mail_or_calendar(self):
        MailboxActions().check_if_authenticated()
        self.choice = input(
            'Do you want to go to email (E) or calendar (C)? You can also give us a feedback (F).')
        if self.choice == 'E':
            self.choice = input(
                'Do you want to read an email (R) or write an email (W)?')
            if self.choice == 'R':
                MailboxActions().read_email()
                self.choice = input(
                    'Do you want to read the body of the email?')
                if self.choice == 'Y':
                    print('\n')
                    MailboxActions().get_body_text()
                    os.system('pause')
                else:
                    os.system('pause')
            elif self.choice == 'W':
                MailboxActions().get_full_mail_info()
                MailboxActions().send_email()
            else:
                En_Start().mail_or_calendar()
        elif self.choice == 'C':
            Read().load_events()
            Read().clear_event()

            os.system("pause")
        elif self.choice == 'F':
            EnSupport().support
            os.system("pause")
        else:
            En_Start().mail_or_calendar()
