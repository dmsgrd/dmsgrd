from django.shortcuts import render
from django.template import RequestContext
# Create your views here.


def home(request):
    title = 'Dmsgrd'


    context = {
        "template_title": title,
    }
    return render(request, "homepage.html", context)


def cv(request):
    title = 'CV'

    context = {
        "template_title": title,
    }
    return render(request, "cv.html", context)