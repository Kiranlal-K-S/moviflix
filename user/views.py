from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from Admin.models import *
from datetime import *

# Create your views here.
def user_home(request):
    info = request.session.get('uid')
    print(info)
    print("------------------------------")
    details=Film.objects.all()
    # film_id=Film.objects.filter(id)
    # like=
    genre=Genre.objects.all()
    context={
        'details':details,
        'info':info,
        'genre': genre,

    }
    return render(request,'user_home.html',context)


def watch_film(request,film_id):
    u_iid=request.session.get('uid')
    if request.method=='POST':
        user_comment=request.POST['user_comment']
        User_comment.objects.create(
            user_comment=user_comment,
            user_id=User_reg.objects.get(id=u_iid),
            film_id=Film.objects.get(id=film_id),
        )

    details=Film.objects.filter(id=film_id)
    comment=User_comment.objects.filter(film_id=film_id)
    cast=Cast.objects.filter(film_id=film_id)
    total_like=Like.objects.filter(film_id=film_id)
    l_count = sum(item.like_count for item in total_like)
    total_dislike=Dislike.objects.filter(film_id=film_id)
    d_count=sum(i.dislike_count for i in total_dislike)

    user_liked = Like.objects.filter(film_id=film_id, user_id=u_iid, like_count=1)
    user_disliked=Dislike.objects.filter(film_id=film_id,user_id=u_iid,dislike_count=1)
    genre=Genre.objects.all()

    context={
        'details':details,
        'comment':comment,
        'l_count':l_count,
        'd_count':d_count,
        'cast':cast,
        'user_liked':user_liked,
        'user_disliked':user_disliked,
        'genre': genre,
    }
    todays_date= datetime.now().date()
    u_id=request.session.get('uid')

    if User_subscription.objects.filter(user_id=u_id).exists():
        end_date = User_subscription.objects.get(user_id=u_id).end_date

        if todays_date>=end_date:
            User_subscription.objects.filter(user_id=u_id).delete()
            return redirect('subsription_page')
        else:
            return render(request,'watch_film.html',context)
    else:
        return redirect('subsription_page')

        
    


def watchlist(request):
     u_id=request.session.get('uid')
     print(u_id)
     details=Watch_list.objects.filter(user_id=u_id)
     genre=Genre.objects.all()
     context={
         'details':details,
         'genre':genre,
     }
     return render(request,'watchlist.html',context)


def add_watchlist(request,film_id):
    u_id=request.session.get('uid')
    if Watch_list.objects.filter(user_id=u_id,film_id=film_id).exists():
        return redirect('user_home')
    Watch_list.objects.create(
        user_id=User_reg.objects.get(id=u_id),
        film_id=Film.objects.get(id=film_id),
    )
    return redirect('user_home')
    
    



def remove_frm_watchlist(request,film_id):
    Watch_list.objects.filter(film_id=film_id).delete()
    
    return redirect('watchlist')



def user_register(request):
    if request.method=="POST":
        u_name=request.POST['u_name']
        u_email=request.POST['u_email']
        u_password=request.POST['u_password']
        c_u_password=request.POST['c_u_password']
        u_number=request.POST['u_number']
        u_address=request.POST['u_address']
        if u_password==c_u_password:
            if User_reg.objects.filter(User_email=u_email,user_password=u_password).exists():
                return redirect('account_already_exists')
            else:

                User_reg.objects.create(
                    u_name=u_name,
                    User_email=u_email,
                    user_password=u_password,
                    u_number=u_number,
                    u_address=u_address,
                )
                return redirect('login_form1')
        else:
            return redirect('confirm_pass')
        
    return render(request,'user_reg.html')


def confirm_pass(request):

    return render(request,'confirm_pass.html')




def login_form(request):
    if request.method=="POST":
        u_email=request.POST['u_email']
        u_password=request.POST['u_password']
        user_detail=User_reg.objects.filter(
             User_email=u_email,
             user_password=u_password,
        )
        if user_detail.exists():
            data = User_reg.objects.filter(User_email=u_email,user_password=u_password).values('u_number', 'id').first()
            request.session['uid'] = data['id']
            request.session['u_num'] = data['u_number']
            request.session['u_email'] = u_email
            request.session['u_pass']=u_password
            return redirect('user_home')
        elif u_email=='admin@gmail.com'and u_password =='12345':
                return redirect('admin_index')
        else:
            return redirect('login_form')
    return render(request,'login.html')



def logout_user(request):
    del request.session['u_email']
    del request.session['u_pass']
    return redirect('login_form1')


def genre_display(request,genre_id):
    genre=Genre.objects.all()
    for i in genre:
        idd=i.id 
        if genre_id == idd:
            name=Genre.objects.filter(id=idd).values('genre_name')
            print(name)
            details= Film.objects.filter(genre_id=idd)
            context={'details':details,
                    'genre': genre,
                    'name': name,}
            return  render(request,'genre.html',context)
    return render(request,'genre.html')



def sample(request):

    return render(request,'sample.html')


def search_film(request):
    
    return render(request,'search_film.html')


def search_show(request):
    if request.method=='POST':
        show_name=request.POST['show_name']
        details=Film.objects.filter(film_name__icontains=show_name)
        context={'details':details,
                 'show_name':show_name}
        return render(request,'search_film.html',context)
    
    return render(request,'search_film.html')



def like(request,film_id):
    uiid=request.session.get('uid')
    film_id=film_id
    if Like.objects.filter(user_id=uiid,like_count=1,film_id=film_id).exists():

        return redirect(f'/watch_film/{film_id}')
    
    elif Dislike.objects.filter(user_id=uiid,dislike_count=1,film_id=film_id).exists() and Like.objects.filter(user_id=uiid,like_count=0,film_id=film_id).exists():
     
        Dislike.objects.filter(user_id=uiid).update(

            dislike_count=0
        )
        Like.objects.filter(user_id=uiid).update(

            like_count=1
        )
        return redirect(f'/watch_film/{film_id}')
    else:
        Like.objects.create(
        user_id=User_reg.objects.get(id=uiid),
        film_id=Film.objects.get(id=film_id),
        )
        Like.objects.filter(user_id=uiid,like_count=0,film_id=film_id).update(
            like_count=1

        )
        Dislike.objects.filter(user_id=uiid,dislike_count=1,film_id=film_id).update(
            dislike_count=0

        )
        return redirect(f'/watch_film/{film_id}')
    

def dislike(request,film_id):
    uiid=request.session.get('uid')
    if Dislike.objects.filter(user_id=uiid,dislike_count=1,film_id=film_id).exists():

        return redirect(f'/watch_film/{film_id}')
    

    elif Like.objects.filter(user_id=uiid,like_count=1,film_id=film_id).exists() and Dislike.objects.filter(user_id=uiid,dislike_count=0,film_id=film_id).exists():
       
        Like.objects.filter(user_id=uiid).update(
            like_count=0
        )
        Dislike.objects.filter(user_id=uiid).update(
            dislike_count=1
        )

        return redirect(f'/watch_film/{film_id}')
    else:
        Dislike.objects.create(
        user_id=User_reg.objects.get(id=uiid),
        film_id=Film.objects.get(id=film_id),
        )
        Dislike.objects.filter(user_id=uiid,dislike_count=0,film_id=film_id).update(
            dislike_count=1

        )
        Like.objects.filter(user_id=uiid,like_count=1,film_id=film_id).update(
            like_count=0

        )
        return redirect(f'/watch_film/{film_id}')
    

def subsription_page(request):
        todays_date= datetime.now().date()
        u_id=request.session.get('uid')

        if User_subscription.objects.filter(user_id=u_id).exists():
            end_date = User_subscription.objects.get(user_id=u_id).end_date

            if todays_date>=end_date:
                User_subscription.objects.filter(user_id=u_id).delete()
                return redirect('subsription_page')
            else:
                return redirect('already_have_subscription')
        else:
            
         u_iid=request.session.get('uid')
         details=User_subscription.objects.filter(id=u_iid)
         subsription_plan=Subcription_plan.objects.all()
    
         context={'subsription_plan':subsription_plan,
                'details':details,}
        if User_subscription.objects.filter(user_id=u_iid).exists():
                print('...............................................................')
                return redirect('already_have_subscription')
        elif request.method=='POST':
            plan = int(request.POST['plan'])
            print(plan)
            
            for i in subsription_plan:
                plans=i.id
                print(plans==plan)
                if plan==plans:
                    start_date=datetime.now().date()
                    dayss=30*i.months_in_numbers
                    User_subscription.objects.create(
                        user_id = User_reg.objects.get(id=u_iid),
                        end_date=start_date + timedelta(days=dayss),
                        )
                    return redirect('subscription_success')
        return render(request,'subscription_plan_display.html',context)

def subscription_success(request):

    return render(request,'subscription_success.html')


def already_have_subscription(request):
     u_iid=request.session.get('uid')
     details=User_subscription.objects.filter(user_id=u_iid)
     context={'details':details}
     return render(request,'already_have_subscription.html',context )

def account_already_exists(request):

    return render(request,'account_already_exists.html')


def login_form1(request):
    if request.method=="POST":
        u_email=request.POST['u_email']
        u_password=request.POST['u_password']
        user_detail=User_reg.objects.filter(
             User_email=u_email,
             user_password=u_password,
        )
        if user_detail.exists():
            data = User_reg.objects.filter(User_email=u_email,user_password=u_password).values('u_number', 'id').first()
            request.session['uid'] = data['id']
            request.session['u_num'] = data['u_number']
            request.session['u_email'] = u_email
            request.session['u_pass']=u_password
            return redirect('user_home')
        elif u_email=='admin@gmail.com'and u_password =='12345':
                return redirect('admin_index')
        else:
            return redirect('login_form1')
    return render(request,'login_form1.html')




    
    
    
    



    



        
        

        
        


    


        

        
        


        









#  def add_comment(request,film_id):
#     if request.method=='POST':
#         user_comment=request.POST['user_comment']
#         u_iid=request.session.get('uid')
#         User_comment.objects.create(
#             user_comment=user_comment,
#             user_id=User_reg.objects.get(id=u_iid),
#             film_id=Film.objects.get(id=film_id),
#         )
#         details=Film.objects.filter(id=film_id)
#         context={'details':details}
#     return redirect('watch_film',context)

    



    




