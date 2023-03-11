from django.shortcuts import render
from .tasks import notify_customer

# Create your views here.


def main(request):
    notify_customer.delay('سلام به روی ماهت')
    return render(request, 'src/main.html')
