import poplib

from email import parser

from email.header import decode_header





server = poplib.POP3('pop.sina.com')
server.user('yangtr09048698@sina.com')
server.pass_('77eb884f8e125563')

resp, mails, octets = server.list()
print('共有 %d 封邮件' % len(mails))

for index in range(len(mails), 0, -1):
    resp, lines, octets = server.retr(index)
    msg_content = b'\r\n'.join(lines).decode('UTF-8')
    msg = parser.Parser().parsestr(msg_content)
    emailbase = {}
    for line in msg.items():
        header = line[0]
        if header in ['From', 'Subject', 'Date']:
            item = decode_header(line[1])[-1]
            code = item[1] if item[1] != None else 'ascii'
            if isinstance(item[0], bytes):
                value = str(item[0], code)
            else:
                value = item[0]
            emailbase[header] = value

    print('-----------%d/%d-----------' %(len(mails) - index + 1, len(mails)))
    print('发件邮箱: ' + emailbase['From'])
    print('信件主题: ' + emailbase['Subject'])
    print('发件时间: ' + emailbase['Date'])

server.quit()
