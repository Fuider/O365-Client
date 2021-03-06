import json
"""beta版本，可选择集成，已知问题已修复。"""


class settings:
    def __init__(self):
        try:
            with open('settings.json', 'r') as sets:
                self.user_sets = json.load(sets)
                self.lang = self.user_sets['lang']
                self.mail_open = self.user_sets['mail_open']
        except FileNotFoundError:
            self.dict = {'lang': '', 'mail_open': ''}
            self.data2 = json.dumps(self.dict)
            with open('settings.json', 'w') as sets:
                sets.write(self.data2)
            with open('settings.json', 'r') as sets:
                self.user_sets = json.load(sets)
                self.lang = self.user_sets['lang']
                self.mail_open = self.user_sets['mail_open']
            print('''你还未设置。You haven't set.''')
            self.set_lang()
            self.set_mail_open()

    def set_lang(self):
        print("""

            请选择语言 Please choose your language:
            [1]简体中文
            [2]English

            """)
        self.lan = input('请输入数字 Please enter the number\n')
        if self.lan == '1':
            self.lan = 'English'
            self.choose_set()
        elif self.lan == '2':
            self.lan = 'Chinese'
            self.choose_set()
        else:
            print('你输入了错误的数字。You entered a wrong number.')
            self.set_lang()

    def choose_set(self):
        choose = input('''您希望设置哪个选项？\n1.语言\n2.加载邮件的方式\n3.退出设置\n请输入对应数字。
        Which do you want to set?\n1. Languages \n2. Mode when loading emails\n3. Quit Settings\nPlease enter the number.
            ''')
        if choose == '1':
            self.set_lang()
        elif choose == '2':
            self.set_mail_open()
        elif choose == '3':
            self.save_sets()
            input('按下回车键以退出 Press Enter to exit')
        else:
            print('您输入了错误的数字！请重新输入\nYou entered a wrong number! Please re-enter.')
            self.choose_set()

    def set_mail_open(self):
        self.open_email_mode = input(
            '请选择阅读邮件时的打开方式\nPlease choose your mode of loading an email\n1.txt\n2.html\n')
        if self.open_email_mode == '1':
            print(
                '您的加载邮件方式已被设为纯文本。Your method of loading emails have been set to txt.')
        elif self.open_email_mode == '2':
            print(
                '您的加载邮件方式已被设为HTML。Your method of loading emails have been set to html.')
        else:
            print(
                '您输入了错误的打开邮件方式代码。请重新输入。\nYou had just entered an incorrect code for loading emails. Please re-enter.')
        self.choose_set()

    def save_sets(self):
        with open('settings.json', 'r') as sets:
            self.ori_set = json.load(sets)
            try:
                self.ori_set['mail_open'] = self.open_email_mode
            except AttributeError:
                self.ori_set['mail_open'] = 1  # 默认纯文本
            try:
                self.ori_set['lang'] = self.lan
            except:
                self.ori_set['lang'] = 'Chinese'
            self.data4 = json.dumps(self.ori_set)
        with open('settings.json', 'w') as wset:
            wset.write(self.data4)

    def load_sets(self):
        with open('settings.json', 'r') as sets:
            self.ori_set = json.load(sets)
            try:
                self.ori_set['mail_open'] = self.open_email_mode
            except AttributeError:
                self.ori_set['mail_open'] = 1  # 默认纯文本
            try:
                self.ori_set['lang'] = self.lan
            except:
                self.ori_set['lang'] = 'Chinese'

