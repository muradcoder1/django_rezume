from django.urls import path
from .views import blog,single_blog
urlpatterns = [
    
    path("single_blog/",single_blog,name="single_blog"),
    path("",blog,name="blog"),
]
    