import smtplib
from datetime import datetime
from mail.tests import password

theme = "Assalamu Alaikum"
sender = "joraev_azam@mail.ru"
reciever = "joraev.azam1252@gmail.com"
given_time = "12:55:00"


def send_mail():
    body = f"Dhuhur Prayer Time 12:16 PM"
    message = f'Subject: {theme}\n\n{body}\n\n{sender}'
    server = smtplib.SMTP("smtp.mail.ru", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, reciever, message)
    server.quit()
    print("Successfully! 587")


while True:
    now = datetime.now().strftime("%H:%M:%S")
    time = datetime.now()
    if now == given_time:
        try:
            send_mail()
        except:
            try:
                delta = datetime.now() - time
                body = f"Dhuhur Prayer Time 12:16 PM\nSorry we are {delta} late due to technical issues."
                message = f'Subject: {theme}\n\n{body}\n\n{sender}'
                server = smtplib.SMTP("smtp.mail.ru", 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(sender, password)
                server.sendmail(sender, reciever, message)
                server.quit()
                print("Successfully! 587")
            except:
                print("Something wrong")