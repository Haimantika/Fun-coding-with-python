import pandas as pd
import smtplib

SenderAddress = "your email address"
password = "your password"

e = pd.read_excel("email.xlsx/the name of the excel file where you have stored the email ids")
emails = e['emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("Your email address", "Your password")
msg = "Hello this is a email form python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail("Your email address", email, body)
server.quit()
