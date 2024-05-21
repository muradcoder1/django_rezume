from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
from django.db import models
from django.db import models
class Upda(models.Model):
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Create Date"
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date"
    )
    class Meta:
        abstract= True
# Create your models here.
class GeneralSetting(Upda):
    name = models.CharField(
        default="",
        max_length=100,
        blank=True,
        help_text='This is for name',
    )
    description=models.CharField(
        default="",
        max_length=254,
        blank=True,
    )
    paramater=models.CharField(
        default="",
        max_length=100,
        blank=True,
    )
   
    class Meta:
        verbose_name = "General Settings"
        verbose_name_plural = "General Settings"
        ordering =("name", "paramater")   



class ImageSetting(Upda):
   name = models.CharField(
        default="",
        max_length=100,
        blank=True,
        help_text='This is for name',
    )
   description=models.CharField(
        default="",
        max_length=254,
        blank=True,
    )
   file=models.ImageField(
       default="",
       blank=True,
       verbose_name="Image",
       upload_to='media/img')
   class Meta:
        verbose_name = "Image Settings"
        verbose_name_plural = "Image Settings"
        ordering= ("file", )
class About(Upda):
    name = models.CharField(
        default="",
        max_length=100,
        blank=True,
        help_text='This is for name',
    )
    description=models.CharField(
        default="",
        max_length=254,
        blank=True,
    )
    text=models.TextField(
        default="",
        max_length=255,
        blank=True,
        )
    class Meta:
        verbose_name = "about"
        verbose_name_plural = "about"
        ordering= ("text", )
class Skills(Upda):
        order=models.IntegerField(
            default=0,
            verbose_name="order",
        )
        name=models.CharField(
            default="",
            blank=True,
            max_length=100,
            verbose_name="Name",
            help_text="This is for name",
        )
        percentage=models.IntegerField(
            default=50,
            verbose_name="Percantage",
            validators=[MinValueValidator(0), MaxValueValidator(100)]



        )
        def __str__(self):
            return f"Skils:{self.name}"
        class meta:
            verbose_name="Skils"
            verbose_name_plural="Skils"
            ordering=("order")

