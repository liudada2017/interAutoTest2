import zmail

#注意subject少用测试或者test,邮箱会自动屏蔽，多了还会被拉黑
class SendEmail:
    def sendOneEmail(self, subject, content_text, attachments):
        mail_content = {
            'subject':subject, #邮件主题
            'content_text':content_text,#邮件内容，邮件正文
            'attachments':attachments   #邮件附件路径
        }

        #发送HTML作为邮件内容
        # with open("report.html",'r',encoding='utf-8') as f:
        #     content_html = f.read()
        # mail_content = {
        #     'subject':'邮件主题',
        #     'content_html':content_html,
        #     "attachments":"report.html"
        #
        # }

        #使用发送邮件的账户和密码，密码是授权码
        server = zmail.server("845809908@qq.com",'nqpjvuofhqydbfba')

        #发送邮件（参数：收件人，邮件内容）
        server.send_mail("845809908@qq.com", mail_content)

        #给多人发送邮件
        #server.send_mail([收件人1，收件人2],邮件内容)