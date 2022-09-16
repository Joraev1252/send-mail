from django.urls import path
from mail.views import send_mail, auto_run


urlpatterns = [
    path('send_mail/', send_mail),
    path('', auto_run)
   ]