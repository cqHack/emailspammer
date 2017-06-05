#!/usr/bin/python

# Made by cqHack

import smtplib
import time

from email.mime.text import MIMEText

server = raw_input("Enter smtp server url > ")
emailsFile = raw_input("Enter filename of emails > ")
content = raw_input("Enter filename of email body > ")
email = raw_input("Enter email of sender > ")
password = raw_input("Enter password of sender > ")

with open(content, "r") as f:
    lines = f.readlines()
    fromName = lines[0]
    subject = lines[1]
    msg = "\n".join(lines[2:])


server = smtplib.SMTP(server, '587')
server.ehlo()
server.starttls()


print("Logging in...")
server.login(email, password)
print("Login complete")

with open(emailsFile, "r") as f:
    emails = f.readlines()

    i = 0
    for recipient in emails:
        i += 1

        mime = MIMEText(msg)
        mime['Subject'] = subject
        mime['From'] = fromName
        mime['To'] = recipient
        server.sendmail(email, recipient, mime.as_string())

        print("On email: {}".format(i))

server.quit()
