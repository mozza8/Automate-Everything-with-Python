import yagmail
import os

sender = '2uporabnik2@gmail.com'

# geslo shranjeni na napravi
passw = os.getenv('PASS')
print(passw)
reciever = 'zanmozoli8@gmail.com'

subject = 'This is the subject'

contents = '''
Here is the content of the email!
Hi!
'''

# SMTP object instance
yag = yagmail.SMTP(user=sender, password=passw)
yag.send(to=reciever, subject=subject, contents=contents)

print("Email Sent!")