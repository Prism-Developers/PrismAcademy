from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'index.html')

def login(request):
    return render(request,'source files/contact.html')