from django.urls import path
from user import views
urlpatterns=[
    path('user_home',views.user_home,name='user_home'),
    path('watch_film/<int:film_id>',views.watch_film,name='watch_film'),
    path('watchlist',views.watchlist,name='watchlist'),
    path('remove_frm_watchlist/<int:film_id>',views.remove_frm_watchlist,name='remove_frm_watchlist'),
    path('user_register',views.user_register,name='user_register'),
    # path('',views.login_form,name='login_form'),
    path('genre_display/<int:genre_id>',views.genre_display,name='genre_display'),
    # path('comedy',views.genre_comedy,name='genre_comedy'),
    # path('war',views.genre_war,name='genre_war'),
    path('sample',views.sample,name='sample'),
    path('search_film',views.search_film,name='search_film'),
    path('search_show',views.search_show,name='search_show'),
    path('add_watchlist/<int:film_id>',views.add_watchlist,name='add_watchlist'),
    # path('add_comment/<int:film_id>',views.add_comment, name='add_comment')
    path('like/<int:film_id>',views.like,name='like'),
    path('dislike/<int:film_id>',views.dislike,name='dislike'),
    path('subsription_page',views.subsription_page,name='subsription_page'),
    path('subscription_success',views.subscription_success,name='subscription_success'),
    path('already_have_subscription',views.already_have_subscription,name='already_have_subscription'),
    path('confirm_pass',views.confirm_pass,name='confirm_pass'),
    path('account_already_exists',views.account_already_exists,name='account_already_exists'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('',views.login_form1,name='login_form1'),
   
]