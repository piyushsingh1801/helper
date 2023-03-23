from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Info
import random
from .handler import MessageHandler
import json
from django.core import serializers

def status(request):
    if request.method == 'POST':
        phn_n = request.COOKIES.get('user')
        profile = Profile.objects.get(phone_number=phn_n)
        profile.activity_status = request.POST.get('activity_status')
        profile.save()
        return render(request, 'home.html')
    

def home(request):
    if request.COOKIES.get('verified') and request.COOKIES.get('verified')!=None:
        if request.method=="POST":
            profession = request.POST.get("profession")
            prof = Profile.objects.filter(profession=profession)
            serialized_queryset = serializers.serialize('json', prof)
            dict_queryset = json.loads(serialized_queryset)
            final_queryset = []
            for i in dict_queryset:
                if i['fields']['activity_status'] == 'on' and i['fields']['phone_number'] != request.COOKIES.get('user'):
                    final_queryset.append(i['fields'])
            for i in final_queryset:
                id = i['user']
                user = User.objects.get(id=id)
                i['user'] = user
            final_queryset_dict ={}
            final_queryset_dict['data'] = final_queryset
            return render(request, 'home.html',context=final_queryset_dict)
        prof = Profile.objects.all()
        serialized_queryset = serializers.serialize('json', prof)
        dict_queryset = json.loads(serialized_queryset)
        final_queryset = []
        for i in dict_queryset:
            if i['fields']['activity_status'] == 'on' and i['fields']['phone_number'] != request.COOKIES.get('user'):
                final_queryset.append(i['fields'])
        final_queryset_dict ={}
        final_queryset_dict['data'] = final_queryset
        for i in final_queryset:
            id = i['user']
            user = User.objects.get(id=id)
            i['user'] = user
        return render(request, 'home.html',context=final_queryset_dict)
    else:
        return HttpResponse("<h1>You are not verified, login first</h1><br><a href='/login/'>login</a>")



def register(request):
    if request.method=="POST":
        if User.objects.filter(username__iexact=request.POST['user_name']).exists():
            return HttpResponse("<h1>User already exists</h1><br><a href='/'>return to registration</a>")
        if Profile.objects.filter(phone_number__iexact=request.POST['phone_number']).exists():
            return HttpResponse("<h1>Phone number already exists</h1><br><a href='/'>return to registration</a>")
        try:
            otp=random.randint(1000,9999)
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()
            user=User.objects.create(username=request.POST['user_name'])
            profile=Profile()
            profile.user = user
            profile.phone_number = request.POST['phone_number']
            profile.profession = request.POST['profession']
            profile.save()
            info = Info()
            info.profile = profile
            info.save()

            red=redirect(f'otp/')
            red.set_cookie("can_otp_enter",otp,max_age=600)
            red.set_cookie("user",request.POST['phone_number'])
            return red
        except:
            return HttpResponse("<h1>Unable to register mobile number! retry</h1><br><a href='/'>Retry</a>")
    return render(request, 'register.html')



def login(request):
    if request.method=="POST":
        if User.objects.filter(username__iexact=request.POST['user_name']).exists():
            profile=Profile.objects.get(phone_number=request.POST['phone_number'])
            profile.activity_status = request.POST['activity_status']
            profile.save()
            otp=random.randint(1000,9999)
            messagehandler=MessageHandler(request.POST['phone_number'],otp).send_otp_via_message()
            red=redirect(f'otp/')
            red.set_cookie("can_otp_enter",otp,max_age=600)
            red.set_cookie("user",request.POST['phone_number'])
            return red
        else:
            return HttpResponse("<h1>Unable to login retry</h1><br><a href='/login/'>Retry</a>") 
    return render(request, 'login.html')



def otpVerify(request):
    if request.method=="POST":
        # profile=Profile.objects.get(uid=uid)     
        if request.COOKIES.get('can_otp_enter')!=None:
            if(request.COOKIES.get("can_otp_enter")==request.POST['otp']):
                red=redirect("home")
                red.set_cookie('verified',True)
                return red
            return HttpResponse("<h1>Wrong OTP</h1><br><a href='/login/'>Retry</a>")
        return HttpResponse("<h1>OTP expired</h1><br><a href='/login/'>Retry</a>")        
    return render(request,"otp.html")



def logout(request):
    var = render(request, 'login.html')
    var.delete_cookie('can_otp_enter')
    var.delete_cookie('verified')
    var.delete_cookie('phone_number')
    return var 


def consult(request):
    username = request.GET['username']
    user = User.objects.get(username=username)

    profile = Profile.objects.get(user=user)

    info = Info.objects.filter(profile=profile)
    serialized_queryset = serializers.serialize('json', info)
    dict_queryset = json.loads(serialized_queryset)
    context = dict_queryset[0]['fields']
    context['username'] = username
    # print(final_queryset)

    return render(request,'consult.html',context)

def pay(request):
    service_seeker = Profile.objects.get(phone_number=request.COOKIES.get('user'))

    service_seeker_info = Info.objects.filter(profile=service_seeker)
    # service_provide = 
    serialized_queryset = serializers.serialize('json', service_seeker_info)
    dict_queryset = json.loads(serialized_queryset)
    print(dict_queryset)

    username = request.GET['username']
    service_provider = User.objects.get(username=username)

    service_provider_profile = Profile.objects.get(user=service_provider)

    service_provider_info = Info.objects.filter(profile=service_provider_profile)
    serialized_queryset = serializers.serialize('json', service_provider_info)
    dict_queryset = json.loads(serialized_queryset)
    print(dict_queryset)

def chatpage(request):
    sender_profile = Profile.objects.filter(phone_number=request.COOKIES.get('user'))
    serialized_queryset = serializers.serialize('json', sender_profile)
    dict_queryset = json.loads(serialized_queryset)
    final_queryset = []
    for i in dict_queryset:
        final_queryset.append(i['fields'])
    for i in final_queryset:
        id = i['user']
        users = User.objects.get(id=id)
    print(User.objects.get(id=8),">>>>>>>>>>>>>>>>>")
    receiver = User.objects.get(username=request.GET['username'])
    # print(receiver.username,receiver.id,"//////////////////")
    # if sender_profile.id > receiver_profile.id:
    #     thread_name = f'chat_{sender_profile.id}-{receiver_profile.id}'
    # else:
    #     thread_name = f'chat_{receiver_profile.id}-{sender_profile.id}'
    # message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'main_chat.html', context={'users': users,'user':receiver})
    
# def room(request, slug):
#     room = Room.objects.get(slug=slug)
#     messages = Message.objects.filter(room=room)[0:25]

#     profile = Profile.objects.get(phone_number=request.COOKIES.get('user'))
#     username = User.objects.get(username=profile.user)

#     return render(request, 'room.html', {'room': room, 'messages': messages,'username':username})