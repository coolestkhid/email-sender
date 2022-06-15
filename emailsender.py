import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Khriss Khringle'
email['to'] = 'khrisskhringle@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'

email.set_content('I am a Python Programmer')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('coolestkhid40@gmail.com', 'KhidInk40')
    smtp.send_message(email)
    print('all good boss')