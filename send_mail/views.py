from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
	send_mail('no subject', 'my message', settings.EMAIL_HOST_USER, ['sourabhs@schooglink.com','shubhamsourabh8@gmail.com','btech15044.18@bitmesra.ac.in'])
	return HttpResponse(202)