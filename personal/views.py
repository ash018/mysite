from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'personal/home.html')
def contact(request):
    return render(request,'personal/basic.html',{'content':['If you like to contact call me @ 01681355216 Or mail me @ sadatakash018@gmail.com']})
