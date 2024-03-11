import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header

if __name__ == "__main__":
    from_addr = "2478395177@qq.com"
    to_addrs = "1044153755@qq.com"
    password = "ilompabkjccxdjja"
    smtp_server = "smtp.qq.com"
    smtp_port = 465

    try:
        # 创建一个SMTP对象
        server = smtplib.SMTP_SSL(smtp_server)  # 使用你的SMTP服务器地址和端口

        msg = MIMEText('Hello, this is a test email.', 'plain', 'utf-8')
        # 设置邮件头部
        msg['From'] = Header("D <2478395177@qq.com>")
        msg['To'] = Header(to_addrs,'utf-8')
        msg['Subject'] = Header("邮件主题", 'utf-8')

        print(msg.as_string())



        # 登录到你的SMTP服务器
        server.login(from_addr, password)

        # 发送邮件

        server.sendmail(from_addr, to_addrs, msg.as_string())

        # 关闭SMTP服务器连接
        server.quit()
        print("发送成功")
    except smtplib.SMTPException as e:
        print(f"Error occurred: {e}")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed, please check your credentials.")
    except smtplib.SMTPServerDisconnected:
        print("SMTP server unexpectedly closed the connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
