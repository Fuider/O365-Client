# O365-Client

\*\*[简体中文(Chinese Simplefied)](https://github.com/Fuider/O365-Client)

The main authors of this program: Micraow, xiaocao162020, ella.

Please read the full document and code of the [python-O365](https://github.com/O365/python-o365) program before you contribute with the program.

The predecessor of this project (O365-Client) is the OMM (O365-Mail-Manager) project.

This project is in the a program which can connect to the Microsoft 365 and operate the emails, see the calendar, etc. We hope we can connect more APIs as much as we can.

We welcome you to have a look at the [branch for Microsoft Graph](https://github.com/Fuider/MSGraph-Client)!

# Contact

You may contact us in many ways: Email: [pengbo@pengbo0708.onmicrosoft.com](mailto:pengbo@pengbo0708.onmicrosoft.com), Telegram: [Click here](https://t.me/fuider)

# Caution

The bug had been fixed. However, the related methods are not integrated.

# Announcement

1. We have changed the goal of developing this program, from only for Microsoft 365 users to all Microsoft users. Which means we will not add the APIs of Planner, Azure Directory, etc. We did this because we do not have enough time, and we have got very less users.

2. The calendar function will request a second time to authorize your account. If there are errors, try deleting the O365_token.txt.

3. We are a group of students who love Information Technology, NOT oen of the Official groups of Microsoft.😂

**We welcome Pull requests and Issues!**
This is our first project, so we are glad if you can help us.
~~From Jul.23th 2020, I will stop the project maintenance, but I will continue do it if I have time.~~
Thanks for the friends in CSDN (P.S.One of China's biggest developers community -A kind note translater xiaocao162020) and Telegram, so I decided to continue doing this program.
The program is very easy. Just use your account to connect our APP ID and secret password and you can operate! We used the [O365](https://github.com/O365/python-o365) project.
If you want to use, please:

1. `pip install O365` Make sure you installed Python, and open CMD, enter 'pip install O365' and wait for it to install.

2.Prepare a Microsoft Account, [click here](https://account.microsoft.com/account?lang=en-us) to sign up. I prefer the E5 subscription of the Microsoft 365. You may Google how to sign up.

That's it! Done!

## About the Microsoft 365 Account

A friend asked me about Microsoft 365 E5 subscription, so I will give you some quick tips here.

1. Go to https://developer.microsoft.com/en-us/office

2. Click 'Start Now', and login your free-signed up Microsoft account.

3. Now it asks you for some information, just enter stuffs about you.

4. Then it will notificate you that you did not sign up for a subsciption, so you add a new one by clicking the '+' button.

5. Then you will get a subsciption of Microsoft 365 E5 for 25 person. You can use your account to login to [Office web app](https://office.com) or the Microsoft 365 apps to enjoy the Microsoft 365 apps and the 5TB onedrive service, etc. If you want to use all the functions normally, you will have to go to the [Admin website](https://admin.microsoft.com) and give your account a subsciption, and you may Google the more functions.

CAUTION: THIS SUBSCIPTION MAY DESPIRE! IF YOU DON'T DO ANY DEVELOPING ACTIVITY 90 DAYS IN A ROLL, MICROSOFT WILL PERMANATELY DELETE YOUR SUBSCIPTION, HERE IS A METHOD TO AUTO-RENEW YOUR SUBSCRIPTION: https://blog.curlc.com/archives/687.html (CHINESE)
MIND: THE ORIGIN STORAGE OF THE ONEDRIVE IS 1TB, YOU HAVE TO CHANGE IT TO 5TB BY THE METHOD HERE: https://blog.curlc.com/archives/66.html

## The using method for users

Run Client.py with your Python interpreter (Python, Python IDLE, PyCharm, Visual Studio Code... .)

## Advantages of our program

1. Succinct, with very little need of storage.
2. Auto renew the token
3. Conform to the style of programming, developers won't be exausted with the designation.
4. More secured.

## Use cases

1. Chinese Users of the Microsoft 365
   The Microsoft 365 is very slow when loading in China mainland, so this program speeds up with not too much loaders.
2. Users that hardly use it
   Not often reading the emails, so they don't want the large software from Microsoft.
3. Users that Log out right after using it
   Very easy! If you want to log out, just delete the O365_token.txt!
4. Geeks
   Using commands to operate, what a great style!!
5. Python lovers
   The program is not very difficult... . You may learn Python with it.

## TO-DO

- ~~Read the calendar events~~
- ~~Send emails~~
- ~~Public Client~~
- Load the body of the email (HTML)
- Load the folders of the users email
- Allow users to edit the emails in txt files
- Delete emails
- Mark this email as read
- Mark as flag
- Mark as unread
- ~~Get object-id~~
- Add an event to the calendar
- The 'support' function
- Move emails to other folders
- Move the function of the calendar to Client.py
- Allow users to search the start time via the name of the event
- Fix bug: When loading html emails, the images cannot be loaded correctly
- Add settings.py，allow users to change the languages (ZH/EN), and change how they want to load their emails (HTML or text)
- Transfer the project
- Search emails by are they read by the user or not.

## Update log

### Jul.24 2020

My O365 Mail Manager is done, have a look!
**The update of this version:**

1. uses public client auth_flow_type=='public'
   (Finally done with this thing which had puzzled me for a day)
2. Allows to choose which email folder to get into.
   Now we support 4: Inbox, Sent, Spam, Deleted.
3. Get the start method from email_actions class, and reconstruct it as 'Start' class, which is the entrance of the app.
4. Optimize most of the code. (Not all)

You can give me a star or join us, thank you for helping me!

### Jul.26

**The update of this version:**
pull from Dreams-builder/O365-Client

### Jul.27

**The update of this version:**
Added the very basic function of sending an email.
xiaocao162020 joins!
Allows multiple email address to send to, thanks to @xiaocao162020

### Aug.8

**The update of this version:**
The sending function is basically done, and we have to improve the return of an html email.

### Aug.11

**The update of this version:**
Added the basic function of Calendar. It can print the name of the events and the start/stop time.

# About the English version document

This English version document is first being written by Micraow, translated by xiaocao162020. This document is translated by hand, and there might be typos, grammatical mistakes, or even register mistakes. We would be glad if you can help us make the program and this document better, just start an Issue, or send us an email, [pengbo@pengbo0708.onmicrosoft.com](mailto:pengbo@pengbo0708.onmicrosoft.com), we will also appreciate if you can join in our Telegram Group: [Click here](https://t.me/fuider).
