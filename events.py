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
from O365.calendar import EventSensitivity
from mailboxactions import MailboxActions
from O365 import Account
import re

credentials = ('74424fcf-55d7-4e15-99d7-1663c0ba2e94', )
account = Account(credentials, auth_flow_type='public')

Mailbox = MailboxActions()
Mailbox.check_if_authenticated()


class Read:
    """专门用来读取日历"""

    def __init__(self):
        pass

    def get_event(self):
        """获取默认日历事件"""
        global events
        for event in events:  # 直接从load_events那里获取
            print(event)

    def clear_event(self):
        """输出经正则表达式处理过的日程（仅名称）"""
        global events
        for event in events:  # 直接从load_events那里获取
            reg = r'Subject:\s(.*?)\s'  # (已修复)就是这里的正则总是报错 未修复:输出结果带Subject:
            # (已修复)就是这里的正则总是报错 re.error: multiple repeat at position 9
            clear_event = re.match(reg, str(event))
            print(clear_event.group())

    def load_events(self):
        """先加载所有事件，这样就可以直接从本地调用，节省时间"""
        global events
        schedule = account.schedule()
        calendar_name = schedule.get_default_calendar()
        print(calendar_name)
        calendar = schedule.get_calendar(calendar_name='Calendar')
        # 说实话，我不知道query有什么用，好像无论赋值什么，都会输出所有日程，所以我删了它。
        events = calendar.get_events(include_recurring=False)

    def event_time(self):
        """(开发中)输出经正则表达式处理过的日程（仅时间）"""
        global events
        for event in events:  # 直接从load_events那里获取
            reg2 = r'Subject:.*?\s(.*?)'  # (已修复)就是这里的正则总是报错 未修复:输出结果带Subject:
            # (已修复)就是这里的正则总是报错 re.error: multiple repeat at position 9
            event_time = re.match(reg2, str(event))
            print(event_time.group())
