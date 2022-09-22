import smtplib
import threading
from datetime import datetime, time
from datetime import date

theme = "Assalamu Alaikum"
sender = "joraev_azam@mail.ru"
reciever = "joraev.azam1252@gmail.com"
password = "xJnmp2v6gEWgKrfJ8euj"

now = datetime.now()
current_hour = now.strftime("%I")
current_min = now.strftime("%M")
current_sec = now.strftime("%S")
current_period = now.strftime("%p")


with open("https://github.com/Joraev1252/send-mail/blob/da0cc19028aaf8ac86c1c2605a843b31197be588/mail/db_file.txt", 'r') as d:
    date_sent = d.read()


def send_mail(body):
    today = date.today()
    message = f'Subject: {theme}\n\n{body}\n\n{sender}'
    server = smtplib.SMTP("smtp.mail.ru", 587)
    if str(today) not in date_sent:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, reciever, message)
        today = date.today()
        with open("https://github.com/Joraev1252/send-mail/blob/da0cc19028aaf8ac86c1c2605a843b31197be588/mail/db_file.txt", 'a') as f:
            f.write(f"{str(today)};")
        server.quit()


def set_interval():
    if datetime.now().strftime("%H:%M") == "12:09":
        body = f"Dhuhur Prayer Time 12:16 PM"
        send_mail(body=body)
    elif datetime.now().strftime("%H:%M") != "12:09":
        hour_delta = int(current_hour) - 12
        min_delta = int(current_min) - 9
        if hour_delta != 0:
            body = f"Dhuhur Prayer Time 12:16 PM, Sorry we are {abs(hour_delta)} hour {abs(min_delta)} minutes late due to technical issues."
        else:
            body = f"Dhuhur Prayer Time 12:16 PM, Sorry we are {abs(min_delta)} minutes late due to technical issues."
        send_mail(body=body)


threading.Timer((datetime.combine(datetime.today(), time(12, 9, 0)) - datetime.now()).total_seconds(), set_interval).start()