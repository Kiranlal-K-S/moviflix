from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from user.models import *

# Create your views here.

def add_form(request):
    genres = Genre.objects.all()
    if request.method =='POST':
        genre_id = request.POST['genre_id']
        film_name=request.POST['film_name']
        film_description=request.POST['film_description']
        film_tumbnail=request.FILES['film_tumbnail']
        film=request.FILES['film']
        Film.objects.create(
            genre_id = Genre.objects.get(id=genre_id),
            film_name=film_name,
            film_description=film_description,
            film_tumbnail= film_tumbnail,
            film=film,
        )
    return render(request,'admin_index.html', {'genres':genres})


def admin_view_c(request):
    details=Film.objects.all()
    context={'cinema_details':details}
    return render(request,'admin_view_cinema.html',context)


def cinema_delete(request,film_id):
    details=Film.objects.filter(id=film_id).delete()
    return redirect('admin_view_u')


def update(request,film_id):
    details=Film.objects.filter(id=film_id)
    genre=Genre.objects.all()
    context={
        'details':details,
        'genre': genre,
    }


    return render(request,'update.html',context)

def update_details(request,film_id):
    if request.method == 'POST':
        film_name = request.POST['film_name']
        film_description = request.POST['film_description']
        genre_id=request.POST['genre_id']
        try:
            film_tumbnail = request.FILES["film_tumbnail"]
            fs= FileSystemStorage()
            file = fs.save(film_tumbnail.name,film_tumbnail)
        except MultiValueDictKeyError:
            file = Film.objects.get(id=film_id).film_tumbnail
        try:
            film = request.FILES["film"]
            fs= FileSystemStorage()
            file2 = fs.save(film.name,film)
        except MultiValueDictKeyError:
            file2 = Film.objects.get(id=film_id).film
        Film.objects.filter(id=film_id).update(
            film_name=film_name,
            film_description=film_description,
            film_tumbnail=file,
            film=file2,
            genre_id=genre_id,
        )
        return redirect('admin_view_u')
    return render(request,'update.html')

def view_user(request):
    details= User_reg.objects.all()
    context={'details':details}
    return render(request,'view_user.html',context)


def del_user(request,user_id):
    User_reg.objects.filter(id=user_id).delete()
    return redirect('view_user')

# --------------------------------------------
def add_form1(request):
    return render(request,'admin_index1.html')



def add_cast(request,film_id):
    details= Film.objects.filter(id=film_id)
    context={
        'details':details,
    }
    if request.method == 'POST':
        actor_name=request.POST['actor_name']
        actor_image=request.FILES['actor_image']
        if Cast.objects.filter(film_id=film_id,actor_name=actor_name).exists():
            return redirect('admin_view_u')
        else:
            Cast.objects.create(
                film_id=Film.objects.get(id=film_id),
                actor_name=actor_name,
                actor_image=actor_image,
            )
            return render(request,'add_cast.html',context)

    return render(request,'add_cast.html',context)

def add_genres(request):
    if request.method == 'POST':
        genre=request.POST['genre']
        Genre.objects.create(
            genre_name=genre,
        )

    return render(request,'add_genres.html')

def add_subscription_plan(request):
    if request.method=='POST':
        months_in_words=request.POST['months_in_words']
        months_in_numbers=request.POST['months_in_numbers']
        plan_price=request.POST['plan_price']
        if Subcription_plan.objects.filter(months_in_words=months_in_words).exists():
            return render(request,'add_subscription_plan.html')
        else:
             Subcription_plan.objects.create(
            months_in_words=months_in_words ,
            months_in_numbers=months_in_numbers,
            plan_price=plan_price,
            )
             return render(request,'add_subscription_plan.html')
    return render(request,'add_subscription_plan.html')

def view_cast(request,film_id):
    cast=Cast.objects.filter(film_id=film_id)
    context={'cast':cast,
             }
    
    return render(request,'view_cast.html',context)

def delete_cast(request,cast_id):
    Cast.objects.filter(id=cast_id).delete()
    return redirect(f'/view_cast/{cast_id}')


def admin_logout(request):
    
    return redirect('login_form1')

def samplee(request):
    return render(request,'sapmlee.html')


 

  


