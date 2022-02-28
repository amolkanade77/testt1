
from email import message

from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail,EmailMessage
import math,random
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

def genrateOTP():
    digits="0123456789"
    OTP=""
    for i in range(8):
        OTP +=digits[math.floor(random.random()*10)]
    return OTP

@csrf_exempt
def send(request):
    email=request.GET.get("email")
    print(email)
    print("Hello")
    o=genrateOTP()
    # current_site=settings.HOST_URL
    # htmlgen='<p> Your OTP is '+o+'</strong></p>'
    # send_mail('OTP request,',o,'<gmail id>',[email],fail_silently=False,html_message=htmlgen)
    # return HttpResponse(o)
    subject='Welcome to amol world'
    message=f'Hi{email},Thank you for Your OTP{o}'
    email_from=settings.EMAIL_HOST_USER
    recept_email=[email]
    msg=EmailMessage(
        subject,
        message,
        email_from,
        recept_email
    )
    msg.content_subtype="html"
    msg.send()
    return HttpResponse(o)


def home(request):
    return JsonResponse({'name':"amol"})

# Create your views here.
