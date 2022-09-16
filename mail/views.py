import smtplib
import requests

from celery.schedules import crontab
from django.http import HttpResponse
from datetime import datetime


def send_mail(request):
    theme = "Assalomu aleykum"
    body = f"Peshin vaqti bo'ldi!"
    sender = "joraev_azam@mail.ru"
    reciever = "joraev.azam1252@gmail.com"
    password = "xJnmp2v6gEWgKrfJ8euj"
    message = f'Subject: {theme}\n\n{body}\n\n{sender}'
    try:
        server = smtplib.SMTP("smtp.mail.ru", 587)
        print("1")
        server.ehlo()
        print("2")
        server.starttls()
        print("3")
        server.ehlo()
        print("4")
        server.login(sender, password)
        print("5")
        server.sendmail(sender, reciever, message)
        print("6")
        server.quit()
        return HttpResponse("Successfully! 587")

    except:
        return HttpResponse("Some thing wrong!")




# import time
#
# seconds = time.time()
# print("Time in seconds since the epoch: ", seconds)
# local_time = time.ctime(seconds)
# print("Local time: ", local_time)
# now = datetime.now().strftime("%H:%M:%S")
# print("Now: ", now)
#
#
# if datetime.now().strftime("%H:%M:%S") == "11:25:32":
#     print("********************")



#
# **********************************
#


print(datetime.now().strftime("%H:%M:%S"))

while True:
    now = datetime.now().strftime("%H:%M:%S")
    given_time = "17:45:00"

    if given_time == now:
        print("******************")
        requests.post('https://send-messagess.herokuapp.com/send_mail/')
        print("requests.post", requests.post('https://send-messagess.herokuapp.com/send_mail/'))
        print("$$$$$$")
        requests.get('https://send-messagess.herokuapp.com/send_mail/')
        print("requests.get", requests.get('https://send-messagess.herokuapp.com/send_mail/'))
        print("end")
