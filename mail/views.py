import smtplib
import schedule
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

from django.http import HttpResponse


def send_mail():
    theme = "Assalomu aleykum"
    body = f"Peshin Vaqti boldi!"
    sender = "joraev_azam@mail.ru"
    # sender = "joraev.azam08@gmail.com"
    reciever = "joraev.azam08@gmail.com"
    # reciever = "joraev_azam@mail.ru"
    password = "xJnmp2v6gEWgKrfJ8euj"
    message = f'Subject: {theme}\n\n{body}'

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
        print("Successfully! 587")

    except:
        print("")
        print("Some thing wrong!")



# while True:
# send_mail()




def auto_send(request):
    schedule.every().day.at("17:48").do(send_mail)
    schedule.run_pending()
    return HttpResponse("send")

    # log = logging.getLogger('apscheduler.executors.default')
    # log.setLevel(logging.INFO)  # DEBUG
    #
    # fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    # h = logging.StreamHandler()
    # h.setFormatter(fmt)
    # log.addHandler(h)
    #
    # print('start to do it')
    #
    # sched = BlockingScheduler()
    #
    # # Schedules job_function to be run on the third Friday
    # #  of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
    # sched.add_job(send_mail, 'cron', day_of_week='mon-fri', hour='17', minute="23", second="00")
    #
    # sched.start()


# def auto_send(request):
#     # schedule.every(10).seconds.do(send_mail)
#     schedule.every().day.at("10:28").do(send_mail)
#
#     # while True:
#     schedule.run_pending()
#     #     time.sleep(1)
#
#     return HttpResponse("Well done!")







