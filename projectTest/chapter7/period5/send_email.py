# -*-coding:utf-8-*-
# pip install smtplib


import smtplib   # 发送邮件
from email.mime.text import MIMEText   # 编写邮件内容
from email.mime.multipart import MIMEMultipart   # 处理多种形态邮件主体
from email.mime.image import MIMEImage   # 处理邮件中的图片
from email.mime.application import MIMEApplication   # 处理附件文件（除图片之外的文件类型）


# 设置登录邮箱数据
smtp_server = 'smtp.qq.com'
sender = '@qq.com'
pwd = '授权码'
receivers = ['@163.com']   # 收件人

# 设置发送的内容
content = '你好，这是发送第二封邮件'
text = MIMEText(content)   # 转化为邮件的文本内容

# 使用MIMEApplication处理txt附件
file = MIMEApplication(open('/projectTest/chapter7/period5/write1.txt', 'rb').read())
file.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', 'write1.txt'))

# 使用MIMEImage处理图片附件
with open('/projectTest/chapter7/period5/img1.png', 'rb') as fp:
    img = MIMEImage(fp.read())
    img['Content-Type'] = 'application/octet-stream'
    img['Content-Disposition'] = 'attachment;filename="img1.png"'

# 将需要发送的内容添加到邮件主体中
txt = MIMEMultipart()   # Multipart 多部件
txt.attach(text)   # attach 贴上，固定
txt.attach(file)
txt.attach(img)
txt['Subject'] = 'send the first email to my number'  # 主题（标题）

# 登录并发送
try:
    smtpObj = smtplib.SMTP()   # 创建 SMTP 对象
    smtpObj.connect(smtp_server, 25)   # 连接服务器，邮箱服务， 端口
    smtpObj.login(sender, pwd)   # 登录邮箱，用户名，密码
    smtpObj.sendmail(sender, receivers, txt.as_string())  # 发送邮件，发送者，收件人，邮件主体
    print('send success')
    smtpObj.quit()   # 退出邮箱登录
except smtplib.SMTPException as e:
    print('send mail error', e)


