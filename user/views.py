from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
# Create your views here.
def userRegister(request):
    username = ''
    email = ''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        telefon = request.FILES['telefon']
        resim = request.FILES['resim']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Kullancı Adı Kullnaımda')
                
            elif User.objects.filter(email= email).exists():
                messages.error(request, 'email kulllanımda')
                

            elif len(password1) < 6:
                messages.error(request, 'şifre en az 6 karakter olması gerekir')
                
            
            elif username in password1 or username.lower() in password1:
                messages.error(request, 'kullanıcı adı ile şifre benzer olamaz')
                
            
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password1, 
                )
                Hesap.objects.create(
                    user = user,
                    image = resim,
                    telefon = telefon
                )
                user.save()
                messages.success(request, 'kullanıcı oluşturuldu')
                return redirect('index')
            
        else:
            messages.error(request, 'şifreler uyuşmuyor')
             

    context = {
        'username':username,
        'email':email
    }          
    return render(request, 'user/register.html', context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'giriş yapıldı')
            return redirect('profiles')
        else:
            messages.error(request, 'Kullancı adı veya şifre hatalı')
            return redirect('login')
    return render(request, 'user/login.html')

def profiles(request):
    profiller = Profile.objects.filter(owner = request.user)
    context = {
        'profiller':profiller
    }
    return render(request, 'user/browse.html', context)


def create(request):
    form = ProfileForm()
    print(Profile.objects.filter(owner = request.user).count())
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if  form.is_valid():
            if Profile.objects.filter(owner = request.user).count() < 4:
                profil = form.save(commit=False)
                profil.owner = request.user
                profil.save()
                messages.success(request, 'profil Oluşturuldu')
                return redirect('profiles')
            else:
                messages.error(request, 'en fazla 4 adet profil oluşturalbailir')
                return redirect('profiles')
    context = {
        'form':form
    }    
    return render(request, 'user/create.html', context)

def hesap(request):
    profil = request.user.hesap
    context = {
        'profil':profil
    }
    return render(request, 'user/hesap.html', context)

def edit(request):
    form = UserForm(instance = request.user)
    hesapForm = HesapForm(instance = request.user.hesap)

    if request.method == 'POST':
        form = UserForm(request.POST, instance = request.user)
        hesapForm = HesapForm(request.POST, request.FILES, instance=request.user.hesap)
        if form.is_valid() and hesapForm.is_valid():
            form.save()
            hesapForm.save()
            messages.success(request, 'Hesabınız güncellendi')
            return redirect('hesap')
    context = {
        'form':form,
        'hesapForm':hesapForm
    }
    return render(request, 'user/edit.html', context)


def change(request):
    myUser = request.user
    if request.method == 'POST':
        eski = request.POST['eski']
        yeni1 = request.POST['yeni1']
        yeni2 = request.POST['yeni2']

        user = authenticate(request, username = request.user, password = eski)

        if user is not None:
            if yeni1 == yeni2:
                myUser.set_password(yeni1)
                myUser.save()
                messages.success(request, 'şifreniz güncellendi')
                return redirect('login')
            else:
                messages.error(request, 'şifreler uyuşmuyor')
                return redirect('change')
        else:
            messages.error(request, 'mevcut şifreniz hatalı') 
            return redirect('change')   
    return render(request, 'user/change.html')

def userLogout(request):
    logout(request)
    messages.success(request, 'çıkış yapıldı')
    return redirect('index')