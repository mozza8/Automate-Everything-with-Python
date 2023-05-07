import yagmail
import os
import time
from datetime import datetime as dt

sender = '2uporabnik2@gmail.com'
passw = os.getenv('PASS')
print(passw)
reciever = 'jelena91@gmail.com'

subject = 'Pozdravljena'

contents = '''
Ti si najlepša punca daleč na okoli. 
Lupčka :) 
'''
while True:
    #now = dt.now()
    #if now.hour == 18 and now.minute == 35:
        yag = yagmail.SMTP(user=sender, password=passw)
        yag.send(to=reciever, subject=subject, contents=contents)
        print("Email Sent!")
        time.sleep(60)