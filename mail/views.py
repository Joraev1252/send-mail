import smtplib
import threading
from threading import Timer
from mail.tests import password
from datetime import datetime, time


theme = "Assalamu Alaikum"
sender = "joraev_azam@mail.ru"
reciever = "joraev.azam1252@gmail.com"

now = datetime.now()
current_hour = now.strftime("%I")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")


def send_mail():
    try:
        if datetime.now().strftime("%H:%M") == "06:00":
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
        elif datetime.now().strftime("%H:%M") != "06:00":
            hour_delta = int(current_hour) - 6
            min_delta = int(current_min) - 0
            sec_delta = int(current_sec) - 0

            if hour_delta != 0:
                body = f"Dhuhur Prayer Time 12:16 PM, Sorry we are {round(abs(hour_delta))} hour {round(abs(min_delta))} minutes late due to technical issues."
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
                body = f"Dhuhur Prayer Time 12:16 PM, Sorry we are {round(abs(min_delta))} minutes late due to technical issues."
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
                body = f"Dhuhur Prayer Time 12:16 PM, Sorry we are {round(abs(sec_delta))} seconds late due to technical issues."
                message = f'Subject: {theme}\n\n{body}\n\n{sender}'
                server = smtplib.SMTP("smtp.mail.ru", 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(sender, password)
                server.sendmail(sender, reciever, message)
                server.quit()
                print("Succesfully! 4")
    except:
        print("Some thing wrong!")


# Timer((datetime.combine(datetime.today(), time(19, 24, 0)) - datetime.now()).total_seconds(), send_mail).start()
threading.Timer((datetime.combine(datetime.today(), time(6, 0, 0)) - datetime.now()).total_seconds(), send_mail).start()
