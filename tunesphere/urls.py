 
from django.urls import include, path
from . import views
 


urlpatterns = [
    path('songs/',views.songs,name='songs'),
    path('songs/<int:id>',views.songpost, name='songpost'),
    path('login',views.login, name='login'),
    path('signup',views.signup, name='signup'),
    # path('',  views.index, name='index'),
    path('watchlater',  views.watchlater, name='watchlater'),
    
    
   
] 
