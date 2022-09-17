import smtplib
import math
from mail.tests import password
from datetime import datetime, time
from threading import Timer


theme = "Assalamu Alaikum"
sender = "joraev_azam@mail.ru"
reciever = "joraev.azam1252@gmail.com"

now = datetime.now()
current_hour = now.strftime("%I")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")


def send_mail():
    if datetime.now().strftime("%H:%M") == "09:00":
        body = f"Dhuhur Prayer Time 12:16 PM"
        message = f'Subject: {theme}\n\n{body}\n\n{sender}'
        server = smtplib.SMTP("smtp.mail.ru", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, reciever, message)
        server.quit()
        print("Succesfully! 1")
    else:
        hour_delta = int(current_hour) - 9
        min_delta = int(current_min) - 0
        sec_delta = int(current_sec) - 5

        if hour_delta != 0:
            body = f"Dhuhur Prayer Time 12:16 PM, Sorry we are {round(math.fabs(hour_delta))} hour {round(math.fabs(min_delta))} minutes late due to technical issues."
            message = f'Subject: {theme}\n\n{body}\n\n{sender}'
            server = smtplib.SMTP("smtp.mail.ru", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender, password)
            server.sendmail(sender, reciever, message)
            server.quit()
            print("Succesfully! 2")

        elif hour_delta == 0 and min_delta != 0:
            body = f"Dhuhur Prayer Time 12:16 PM, Sorry we are {round(math.fabs(min_delta))} minutes late due to technical issues."
            message = f'Subject: {theme}\n\n{body}\n\n{sender}'
            server = smtplib.SMTP("smtp.mail.ru", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender, password)
            server.sendmail(sender, reciever, message)
            server.quit()
            print("Succesfully! 3")

        elif hour_delta == 0 and min_delta == 0 and sec_delta != 0:
            body = f"Dhuhur Prayer Time 12:16 PM, Sorry we are {round(math.fabs(sec_delta))} seconds late due to technical issues."
            message = f'Subject: {theme}\n\n{body}\n\n{sender}'
            server = smtplib.SMTP("smtp.mail.ru", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender, password)
            server.sendmail(sender, reciever, message)
            server.quit()
            print("Succesfully! 4")


Timer(
    (datetime.combine(
        datetime.today(), time(9, 0, 5)
    ) - datetime.now()).total_seconds(),
    send_mail
).start()
