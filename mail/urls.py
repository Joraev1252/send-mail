from django.urls import path, include
from mail.views import send_mail


urlpatterns = [
    path('send_mail/', send_mail),
    # path('auto_send/', auto_send)
   ]
