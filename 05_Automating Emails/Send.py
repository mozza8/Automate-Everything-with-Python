import yagmail
import os

sender = '2uporabnik2@gmail.com'

# geslo shranjeni na napravi
passw = 'kfkomocudiajncsb'
reciever = 'jelena91@gmail.com'

subject = 'Pozdravljena'

contents = '''
Ti si najlepša punca daleč na okoli. 
Lupčka Žan :) 
'''

# SMTP object instance
yag = yagmail.SMTP(user=sender, password=passw)
yag.send(to=reciever, subject=subject, contents=contents)

print("Email Sent!")