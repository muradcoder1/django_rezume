from django.urls import path
from .views import index,about_us,services,portfolio,elements,blog,single_blog,contact
urlpatterns = [
    path("",index, name="index"),
    path("about-us/",about_us,name="about-us"),
    path("services/",services,name="services"),
    path("portfolio/",portfolio,name="portfolio"),
    path("elements/",elements,name="elements"),
    path("blog/",blog,name="blog"),
    path("single_blog/",single_blog,name="single_blog"),
     path("contact/",contact,name="contact"),
]