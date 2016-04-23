from django.shortcuts import render
# Create your views here.


def home(request):
    title = "Dmsgrd"

    context = {
        "template_title": title,
    }
    return render(request, "homepage.html", context)

