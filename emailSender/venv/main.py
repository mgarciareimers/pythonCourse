import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

print('* Welcome to email sender with gmail account')
email = EmailMessage()

print('  Preparing email...')

email['from'] = 'Sender Name'
email['to'] = 'account.to@gmail.com'
email['subject'] = 'Email Subject'

# Prepare message.
print('  Preparing message as HTML...')
html = Template(Path('emailTemplate.html').read_text())
email.set_content(html.substitute(name='Name'), 'html')

print('  Preparing host...')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email.from@gmail.com', 'passwordFrom')

    print('  Sending email...')

    smtp.send_message(email)

    print('* The email has been sent!')
