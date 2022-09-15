import smtplib
from django.http import HttpResponse


def send_mail():
    theme = "Assalomu aleykum"
    body = f"Peshin Vaqti boldi!"
    sender = "joraev_azam@mail.ru"
    # sender = "joraev.azam08@gmail.com"
    reciever = "joraev.azam08@gmail.com"
    # reciever = "joraev_azam@mail.ru"
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

        print("")
        return HttpResponse("Successfully! 587")

    except:
        print("")
        return HttpResponse("Some thing wrong!")


if __name__ == "__views__":
    send_mail()


