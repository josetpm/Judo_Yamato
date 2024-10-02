from django.shortcuts import redirect, render
from .forms import *


def home_view(request):
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect("home")
    else:
        form = NewForm()
    news = News.objects.all()
    return render(request, "home.html", {"form": form, "news": news})


def calendar_view(request):
    return render(request, "calendar.html")
