from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'about.html')
def allstates(request):

    if request.method=="GET":
        name=request.GET['txtname']
        print(name)
        password =request.GET['txtpswd']
        print(password)
        if name=="madhu" and password=="Rmadhu123":
            return render(request, 'state.html')
        else:
            return HttpResponse('<h1>invalid details</h1>')




