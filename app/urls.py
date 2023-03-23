from django.urls import path

from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('otp/', views.otpVerify, name='otp'),
    path('otp/home/',views.otpVerify),
    path('login/otp/', views.otpVerify, name='otp'),
    path('logout/',views.logout,name='logout'),
    path('status/',views.status),
    path('consult/',views.consult),
    path('pay/',views.pay,name='pay'),
    path('chat/',views.chatpage,name='rooms'),
    # path('room/<str:slug>',views.room,name='room'),

]
