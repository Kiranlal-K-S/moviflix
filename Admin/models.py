from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_name = models.CharField(max_length=120)

    def __str__(self):
        return self.genre_name

class Film(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    film_name=models.CharField(max_length=50)
    film_description=models.CharField(max_length=200)
    film_tumbnail=models.ImageField(upload_to='film_tumbnail',default='null.jpg')
    film=models.FileField(upload_to='film_f',default='null.mp4')
    w_count=models.IntegerField(default=0)

    def __str__(self):
        return self.film_name

class Cast(models.Model):
    film_id=models.ForeignKey(Film,on_delete=models.CASCADE)
    actor_name=models.CharField(max_length=20)
    actor_image=models.FileField(upload_to='film_cast',default='null.jpg')

class Subcription_plan(models.Model):
    months_in_words=models.CharField(max_length=12)
    months_in_numbers=models.IntegerField()
    plan_price=models.IntegerField()