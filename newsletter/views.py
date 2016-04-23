from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.


def home(request):
    title = "Dmsgrd"


    form = SignUpForm()
    context = {
        "template_title": title,
        "form": form
    }
    return render(request, "home.html", context)


