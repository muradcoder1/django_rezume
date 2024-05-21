from django.shortcuts import render
from .models import GeneralSetting, ImageSetting,About,Skills
# Create your views here.
def index(request): 
    site_title=GeneralSetting.objects.get(name="site_title").paramater
    profile=ImageSetting.objects.get(name="profile").file
    position=GeneralSetting.objects.get(name="position").paramater
    skills=Skills.objects.all()
    about=About.objects.get(name="UP").text
    about1=About.objects.get(name="second").text
    context={
        "site_title":site_title,
         "profile":profile,
         "position":position,
         "about":about,
         "about1":about1,
          "skills": skills

         
         
    }
    return render(request, "index.html",context)
def about_us(request):
    return render(request, "about-us.html")
def services(request):
    return render(request, "services.html")
def portfolio(request):
    return render(request, "portfolio.html")
def elements(request):
    return render(request, "elements.html")

