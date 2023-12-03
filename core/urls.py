from django.urls import path
from . import  views


urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.Logout,name='logout'),
    path('settings/',views.Settings,name='settings'),
    path('upload/',views.upload,name='upload'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('like-post',views.Like_Post,name='like-post'),
    path('follow/',views.follow,name='follow'),
    path('search/',views.search,name='search')
]

