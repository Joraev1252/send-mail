from django.http import HttpResponse
from django.shortcuts import render
import smtplib



def send_mail(request):
    theme = "Assalomu aleykum"
    body = "Peshin Vaqti boldi!"
    sender = "joraev_azam@mail.ru"
    reciever = "joraev_azam@mail.ru"
    # reciever = "joraev.azam1252@gmail.com"
    password = "JsnkpW0vizyNVcYNbarY"

    message = f'Subject: {theme}\n\n{body}'

    try:
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



# send_mail()



