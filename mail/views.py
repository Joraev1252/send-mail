import smtplib
from django.http import HttpResponse
import requests
from datetime import datetime
import requests
from datetime import datetime


def send_mail():
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
        print("Successfully! 587")

    except:
        print("Some thing wrong!")


# def auto_run(request):
#     print(datetime.now().strftime("%H:%M:%S"))
#     while True:
#         now = datetime.now().strftime("%H:%M:%S")
#         given_time = "20:56:00"
#         time = "20:57:00"
#         if given_time == now or time == now:
#             print("******************")
#             requests.post('https://send-messagess.herokuapp.com/send_mail/')
#             print("$$$$$$")


# now = datetime.now().strftime("%H:%M:%S")
# given_time = "21:51:00"


while True:
    now = datetime.now().strftime("%H:%M:%S")
    given_time = "21:59:00"
    if given_time == now:
        send_mail()
