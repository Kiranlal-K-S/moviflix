from django.urls import path
from Admin import views

urlpatterns=[
    path('admin_index',views.add_form,name='admin_index'),
    path('admin_view_c',views.admin_view_c,name='admin_view_u'),
    path('cinema_delete/<int:film_id>',views.cinema_delete,name='cinema_delete'),
    path('update/<int:film_id>',views.update,name='update'),
    path('update_details/<int:film_id>',views.update_details,name='update_details'),
    path('view_user',views.view_user,name='view_user'),
    path('del_user/<int:user_id>',views.del_user,name='del_user'),
    # -----------------------------------------------------------
    path('add_form1',views.add_form1,name='add_form1'),
    path('add_cast/<int:film_id>',views.add_cast,name='add_cast'),
    path('add_genres',views.add_genres,name='add_genres'),
    path('add_subscription_plan',views.add_subscription_plan,name='add_subscription_plan'),
    path('view_cast/<int:film_id>',views.view_cast,name='view_cast'),
    path('delete_cast/<int:cast_id>',views.delete_cast,name='delete_cast'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
]