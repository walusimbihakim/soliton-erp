from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def login_page(request):
    return render(request, "auths/login.html")

def index_page(request):
    return render(request, "auths/index.html")
    # return HttpResponseRedirect(reverse('dashboard_page'))