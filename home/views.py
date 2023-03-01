from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def main(request):
    send_mail('Welcome', 'Hello world i am back', 'shadino@mail.com', ['behshad.rahmanpour@gmail.com'])
    return render(request, 'src/main.html')
