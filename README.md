# O365-Client

本程序真实维护人,主要人员:Micraow

在为本项目做出贡献前，请仔细阅读python-o365 项目的文档，及全部代码  [传送门](https://github.com/O365/python-o365)

此项目(O365-Client)为原OMM(O365-Mail-Manager)项目

用Python编写的代码示例，与O365连接并查阅邮件，查看日历等。我们的梦想是尽可能多的集成API。

**欢迎Pull requests和Issues!**

这是我第一个独立的项目，希望大家支持。
~~自2020.7.23起，此项目将不再定期维护，但如果以后有时间，我将会继续做下去。~~
感谢csdn和电报中众多朋友的帮助，现在我决定继续维护这个项目。
程序很简单，通过我的应用ID和机密连接到你的账号，并操作，运用了一个模板 [O365](https://github.com/O365/python-o365 "O365").
如果你要使用，请：

1. `pip install O365`

2.准备一个微软账号 [注册](https://account.microsoft.com/account?lang=zh-cn) ，事实上我更推荐含Office 365(现更名为Microsoft 365)的E5开发者订阅（我用的就是这个比较靠谱，而且可以支持所有的API），注册方法请自行百度。

没了，就这么简单！

### 关于office 365账户
有一位朋友跟我讲说他需要获取office E5订阅
那么我就在这里讲一下大致的步骤。
1. 访问微软的开发者网站 https://developer.microsoft.com/zh-cn/office

2. 按下"立即加入"，或"了解更多信息"，接下来你需要登录你注册的免费的微软账号。
![](https://share.pengbo.workers.dev/1595596248544.jpg)

3. 然后它会要你填些信息，随便填一填就好了。

4. 然后它会提示你没有订阅，按左边的加号新建一个，这过程因为要通过谷歌的验证码进行验证，所以需要科学上网，准备好工具。

5.然后你添加完之后就能拿到一个有25位用户许可证的E5订阅，包含了全套的office套件，可用来正版激活软件，就不用熊那些么盗版的激活工具了，只要登录你的账号就可以激活办公软件了，不止支持软件的激活，这个订阅还包括了每个用户都有5 TB的云存储空间，还有你可以给他们分配邮箱。我的做法是给我的朋友们分配了这些邮箱，然后我便可以与他们联系。
[Office 网页版](https://office.com)
[管理员网站](https://admin.microsoft.com)
如果想要正常使用所有功能，需要在管理员网站中为你的主账户，就是默认生成的那个账户，也就是管理员账户分配一个许可证(E5)
此时你所有的邮箱后缀都为.onmicrosoft.com 如果你想要自定义后缀的话，可以绑定自定义域名，当然这些都是后话了，请自行百度。

需要注意的是，这个订阅是会过期的！如果90天内不进行开发活动(其实也有自动续订的方法)，微软就会删除你的订阅，这里推荐一个自动续订的方法
https://blog.curlc.com/archives/687.html
如果你觉得我讲的不够详细。那么你可以看一看这篇文章。
https://blog.curlc.com/archives/599.html
提醒:onedrive 默认的存储容量为1 TB，需要将他们手动改为5 TB，当然，1TB=1024 GB，相当于百度网盘的容量。你如果直连下载onedrive 的文件的话，速度可能只比百度云快一点点，虽然微软没有对其进行限速，因为onedrive 的服务器在国外，你可以搭建oneindex(如果你使用的是自己的应用ID和机密，还可以提高续订的概率，因为据说微软时看API的调用量判断你的开发是否活跃。使用本程序也可以调用API，虽然调用的是我的[偷笑]但是你可以换成你的，具体怎么换？我过一段时间回写下来。) 或其他的索引，或者一些在线的工具获取下载直链，然后通过idm多线程下载速度很快。
具体如何更改onedrive的容量，请看这篇文章。
https://blog.curlc.com/archives/66.html

## 面向用户的使用方法

运行Client.py

## 优点
1. 简洁，体积小
2. 后台自动刷新token，无需烦恼
3. 基本符合类编程风格，开发人员看的时候省心
4. 使用公共客户端流，更安全！

## 使用场景
1. 大陆O365用户
   由于GFW的封锁，访问O365网页版服务时，加载js，脚本，页面等会用很长时间，使用本程序就简化了这些，提高效率。
2. 轻度用户
   不经常看邮箱，日历，只偶尔看一下，不想要下载微软那么大的软件。
3. 即用即退的用户
   本程序登录简单，注销也简单。将...token.txt删去即可。
4. 极客，发烧友
   在终端命令行操作，范儿立马就有了！
5. Python爱好者，学者，小白
   并不是很难，可以做代码示例学习。

## TO-DO
 - 日历功能（读取）
 - ~~发送邮件~~
 - ~~公共客户端问题。~~
 - 加载邮件全文(HTML)
 - 加载用户邮件文件夹
 - 允许用户在txt文件中编辑邮件，然后程序识别，发送，有利于排版。
 - 删除邮件
 - 标为已读
 - 标为红旗
 - 标为未读
 - 获取object-id
 - 新建日历日程
 - 支持 功能
 - 移动邮件

## 更新日志
### 2020.7.24

我的开源项目O365 Mail Manager终于完工了，大家有兴趣的快去看看吧。
本次更新内容:
1. 使用公共客户端流auth_flow_type=='public'
(终于解决了困扰了我一天的难题)
2. 允许选择进入哪个邮箱文件夹
当前有四个是支持的。
3. 将start方法从email_actions类中重构出来，使之成为Start类(应用入口)
4. 优化部分代码，使其符合类编程风格。(还没优化完全部)

喜欢的可以给个star或与我合作，谢谢你们给了我动力！

### 7.26

更新内容:
拉取至Dreams-builder/O365-Client

### 7.27

有了最基础的发件功能。
xiaocao162020加入！
支持多收件人，感谢 @xiaocao162020

### 8.8
发件功能基本实现，但HTML邮件处理要改善。
