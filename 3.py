import smtplib

from email.mime.text import MIMEText

mailto_list=["18211033286@163.com"]
mail_host = "smtp.sina.com"
mail_user = 'yangtr09048698@sina.com'
mail_pass = '77eb884f8e125563'


msg = MIMEText('test1')
msg['Subject'] = ('test1')
msg['From'] = mail_user
msg['To'] = ';'.join(mailto_list)

s = smtplib.SMTP()
s.connect(mail_host)
s.login(mail_user, mail_pass)
s.sendmail(mail_user, mailto_list, msg.as_string())
s.close()

print('成功')

try:
    S = smtp.SMTP()
    S.connect(mail_host)
    S.login(mail_user, mail_pass)
    S.sendmail(mail_user, mailto_list, msg.as_string())
    S.close()
    print('Success')

except Exception:
    print(str(Exception))
    print('Fail')
