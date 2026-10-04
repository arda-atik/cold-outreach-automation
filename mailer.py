import os
import random
import smtplib
import time

email = os.getenv("GMAIL_USER")
password = os.getenv("GMAIL_APP_PASSWORD")

with open("leads.txt", "r") as file:
  leads = file.read().splitlines()

subject = "Subject: Hello\n\n"
content = "Hi,\nThis is a short message.\n\nBest,\nStudent"
message = subject + content

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(email, password)

for lead in leads:
  if "@" in lead:
    server.sendmail(email, lead, message)
    print("Sent to:", lead)
    time.sleep(random.randint(5, 10))

server.quit()
print("Done!")
