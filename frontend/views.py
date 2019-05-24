from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from django.http import HttpResponse

class HomeView(View):
    def get(self, request, *arg, **kwargs):
        return render(request, "pages/home.html", {"register": "ssss", "canApprove": False})

    
# def index(request):
#     return HttpResponse("Hello World")