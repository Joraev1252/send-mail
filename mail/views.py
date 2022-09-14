import datetime

from django.http import HttpResponse
from django.shortcuts import render
import smtplib
import schedule
import time
from requests import request


def send_mail():
    theme = "Assalomu aleykum"
    body = f"Peshin Vaqti boldi!{datetime.datetime.now()}"
    sender = "joraev_azam@mail.ru"
    reciever = "joraev_azam@mail.ru"
    # reciever = "joraev.azam1252@gmail.com"
    password = "JsnkpW0vizyNVcYNbarY"

    message = f'Subject: {theme}\n\n{body}'

    try:
        print("0")
        server = smtplib.SMTP("smtp.mail.ru", 2525)
        print("1")
        # server.connect("smtp.gmail.com", 587)
        print("2")
        server.ehlo()
        print("3")
        server.starttls()
        print("4")
        server.ehlo()
        print("5")

        server.login(sender, password)
        print("6")

        server.sendmail(reciever, sender, message)
        print("7")
        server.quit()

        print("")
        # print("Successfully!")
        return HttpResponse("Successfully!")
    # try:
    #     print("1")
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     print("2")
    #     server.ehlo()
    #     print("3")
    #     server.starttls()
    #     print("4")
    #     server.ehlo()
    #     print("5")
    #
    #     server.login(sender, password)
    #     print("6")
    #
    #     server.sendmail(reciever, sender, message)
    #     print("7")
    #     server.quit()
    #
    #     print("")
    #     print("Successfully!")

    except:
        print("")
        # print("Some thing wrong!")
        return HttpResponse("Some thing wrong!")


def auto_send(request):
    # schedule.every(10).seconds.do(send_mail)
    schedule.every().day.at("18:56").do(send_mail)

    while True:
        schedule.run_pending()
        time.sleep(1)
    # while time_send:
    #     schedule.run_pending()
    #     time.sleep(1)
    # return HttpResponse("Well done!")








