#  O365-Client -- A client to connect O365
#  Copyright (C) 2020  Xiaocao162020
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
import time
import os

lang_exists = os.path.isfile("lang")
# 未完成，返回bool，true则判断中英文，false则二语言。


class Setlang:
    def set_language(self):
        entered_lancode_right = False
        while not entered_lancode_right:
            self.language = input(
                '请选择语言\nPlease choose your language:\n1.ZH\n2.EN\n')
            if self.language == '1':
                f1 = open("lang", encoding='utf-8', mode='w')
                f1.write(self.language)
                f1.close()
                print('您的语言已经被设为中文。\n')
                entered_lancode_right = True
                time.sleep(2)
            elif self.language == '2':
                f1 = open('lang', encoding='utf-8', mode='w')
                f1.write(self.language)
                f1.close()
                print('Your language had been set to English.')
                entered_lancode_right = True
                time.sleep(2)
            else:
                print(
                    '您输入了错误的语言代码。请重新输入。\nYou had just entered an incorrect code for languages. Please re-enter.')
                time.sleep(3)

    def set_openemail_mode(self):
        entered_mailopencode_right = False
        if lang_exists == True:
            f4 = open('lang', encoding='utf-8', mode='r')
            msg = f4.read
            if msg == '1':
                while not entered_mailopencode_right:
                    self.open_email_mode = input(
                        '请选择阅读邮件时的打开方式\n1.txt\n2.html)')
                    if self.open_email_mode == '1':
                        f2 = open('emailloadmethod',
                                  encoding='utf-8', mode='w')
                        f2.write(self.open_email_mode)
                        f2.close()
                        print('您的加载邮件方式已被设为纯文本。')
                        entered_mailopencode_right = True
                        time.sleep(2)
                    elif self.open_email_mode == '2':
                        f2 = open('emailloadmethod',
                                  encoding='utf-8', mode='w')
                        f2.write(self.open_email_mode)
                        f2.close()
                        print('您的加载邮件方式已被设为HTML。')
                        entered_mailopencode_right = True
                        time.sleep(2)
                    else:
                        print('您输入了错误的打开邮件方式代码。请重新输入。\n')
                        time.sleep(3)
            elif msg == '2':
                while not entered_mailopencode_right:
                    open_email_mode = input(
                        'Please choose your mode of loading an email\n1.txt\n2.html)')
                    if open_email_mode == '1':
                        f2 = open('emailloadmethod',
                                  encoding='utf-8', mode='w')
                        f2.write(open_email_mode)
                        f2.close()
                        print('Your method of loading emails have been set to txt.')
                        entered_mailopencode_right = True
                        time.sleep(2)
                    elif open_email_mode == '2':
                        f2 = open('emailloadmethod',
                                  encoding='utf-8', mode='w')
                        f2.write(open_email_mode)
                        f2.close()
                        print('Your method of loading emails have been set to html.')
                        entered_mailopencode_right = True
                        time.sleep(2)
                    else:
                        print(
                            'You had just entered an incorrect code for loading emails. Please re-enter.\n')
                        time.sleep(3)
        while not entered_mailopencode_right:
            open_email_mode = input(
                '请选择阅读邮件时的打开方式\nPlease choose your mode of loading an email\n1.txt\n2.html)')
            if open_email_mode == '1':
                f2 = open('emailloadmethod', encoding='utf-8', mode='w')
                f2.write(open_email_mode)
                f2.close()
                print(
                    '您的加载邮件方式已被设为纯文本。Your method of loading emails have been set to txt.')
                entered_mailopencode_right = True
                time.sleep(2)
            elif open_email_mode == '2':
                f2 = open('emailloadmethod', encoding='utf-8', mode='w')
                f2.write(open_email_mode)
                f2.close()
                print(
                    '您的加载邮件方式已被设为HTML。Your method of loading emails have been set to html.')
                entered_mailopencode_right = True
                time.sleep(2)
            else:
                print(
                    '您输入了错误的打开邮件方式代码。请重新输入。\nYou had just entered an incorrect code for loading emails. Please re-enter.')
                time.sleep(3)

    def choose_set(self):
        not_quitted = True
        while not_quitted:
            choose = input('''您希望设置哪个选项？\n1.语言\n2.加载邮件的方式\n3.退出设置\n请输入对应数字。
        Which do you want to set?\n1. Languages \n2. Mode when loading emails\n3. Quit Settings\nPlease enter the number.
            ''')
            if choose == '1':
                self.set_language()
            elif choose == '2':
                self.set_openemail_mode()
            elif choose == '3':
                not_quitted = False
            else:
                print('您输入了错误的数字！请重新输入\nYou entered a wrong number! Please re-enter.')
