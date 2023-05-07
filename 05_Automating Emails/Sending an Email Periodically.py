import yagmail
import os
import time

sender = '2uporabnik2@gmail.com'
passw = os.getenv('PASS')
print(passw)
reciever = 'aebgnajhkkbibc@dropmail.me'

subject = 'This is the subject'

contents = '''
Here is the content of the email!
Hi!
'''
while True:
    yag = yagmail.SMTP(user=sender, password=passw)
    yag.send(to=reciever, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)