from django.shortcuts import redirect, render
from .forms import *


def home_view(request):
    if request.method == "POST":
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                new = form.save(commit=False)
                new.save()
                return redirect("home")
            except Exception as e:
                print(f"Error saving new: {e}")
                form.add_error(None, "Error al guardar la noticia.")
        else:
            print(form.errors)
    else:
        form = NewForm()
    news = News.objects.all()
    return render(request, "home.html", {"form": form, "news": news})


def calendar_view(request):
    return render(request, "calendar.html")
