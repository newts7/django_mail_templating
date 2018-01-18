from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from mail_templated import  send_mail
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    #x = send_mail(template_name='hello.tpl',context='testing',from_email='srivastavadi12@gmail.com',recipient_list=['divyanshu@betterhalf.ai'],auth_user='srivastavadi12@gmail.com',auth_password='iloveashna')
    msg_html = render_to_string('index.html', {'some_params': 'some_params'})
    send_mail(subject="tesitng",message="khel rahe hain",html_message=msg_html,from_email='srivastavadi12@gmail.com',recipient_list=['divyanshu@########.ai'])
    return HttpResponse({'Hello World'},status=200)
