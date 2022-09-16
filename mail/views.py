import smtplib
from django.http import HttpResponse
import requests
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


def auto_run(request):
    print(datetime.now().strftime("%H:%M:%S"))
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        given_time = "20:10:00"
        if given_time == now:
            print("******************")
            requests.post('https://send-messagess.herokuapp.com/send_mail/')
            print("$$$$$$")
