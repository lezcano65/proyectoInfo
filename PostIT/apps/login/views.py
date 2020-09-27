from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse_lazy

from apps.user.forms import LoginForm, registernota, registerUser
from apps.user.models import nota
from apps.user.views import mostrar_notas

from .forms import changeUsernameForm, changeEmailForm, changePassForm

# from django.contrib import messages


def indexPage(request):
    if request.method == "POST":
        log_in = LoginForm(request.POST)
        model_username = request.POST.get('username')
        model_password = request.POST.get('password')
        if (model_username != None) and (model_password != None):
            if log_in.is_valid():
                user = authenticate(username=model_username,
                                    password=model_password)
                login(request, user)
                # messages.success(request, 'User name is: '+model_username)
                current_user = request.user
                user = User.objects.get(username=model_username)
                return mostrar_notas(request)
            else:
                # messages.success(request, 'data error :')
                return redirect('index')
    newUser = registerUser(request.POST)
    model = User
    if newUser.is_valid():
        model.username = newUser.cleaned_data["username"]
        model.email = newUser.cleaned_data["email"]
        model.password1 = newUser.cleaned_data["password1"]
        model.password2 = newUser.cleaned_data["password2"]
        grabar = User(username=model.username, email=model.email,
                      password=model.password1)
        if (model.password1 == model.password2):
            grabar.save()
            user = User.objects.get(username=model.username)
            user.is_staff = True
            user.is_active = True
            user.set_password(model.password1)
            user.save()
            username = newUser.cleaned_data.get('username')
            password = newUser.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return mostrar_notas(request)
            # messages.success(request, 'New user create whit name '+model.username)
    else:
        newUser = registerUser()
        log_in = LoginForm()
    return render(request, 'login/index.html', {'newUser': newUser, "log_in": log_in})


@login_required
def logoutUser(request):
    logout(request)
    return redirect('index')


@login_required
def settingsUser(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    ctx = {"user": user}
    return render(request, 'login/settings.html', ctx)

 # permiso para usuario


def changeEmail(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == "POST":
        newUser = changeEmailForm(request.POST)
        model_email = request.POST.get("email")
        model_email2 = request.POST.get('email2')
        model_email3 = request.POST.get('email3')
        if model_email2 != model_email:
            grabar = User(id=user.id, username=user.username, email=model_email2,
                          password=user.password)
            if (model_email2 == model_email3):
                grabar.save()
                user = User.objects.get(id=current_user.id)
                user.is_staff = True
                user.is_active = True
                user.set_password(user.password)
                user.save()
                return redirect('home')
            else:
                print("contraseña no coincide")
                return redirect('changeEmail')
        else:
            print("formulario invalido")
            return redirect('changeEmail')
    else:
        newUser = changeEmailForm()
    return render(request, "login/changeEmail.html", {'User': newUser})


@login_required
def changeUsername(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == "POST":
        newUser = changeUsernameForm(request.POST)
        model_username = request.POST.get("username")
        model_username2 = request.POST.get('username2')
        model_username3 = request.POST.get('username3')
        if model_username2 != model_username:
            grabar = User(id=user.id, username=model_username2, email=user.email,
                          password=user.password)
            if (model_username2 == model_username3):
                grabar.save()
                user = User.objects.get(id=current_user.id)
                user.is_staff = True
                user.is_active = True
                user.set_password(user.password)
                user.save()
                user = authenticate(username=user.username,
                                    password=user.password)
                login(request, user)
                return redirect('home')
            else:
                print("contraseña no coincide")
                return redirect('changeUsername')
        else:
            print("formulario invalido")
            return redirect('changeUsername')
    else:
        newUser = changeUsernameForm()
    return render(request, "login/changeUsername.html", {'User': newUser})


@login_required
def changePass(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    if request.method == "POST":
        newUser = changePassForm(request.POST)
        model_pass = request.POST.get("pass")
        model_pass2 = request.POST.get('pass2')
        model_pass3 = request.POST.get('pass3')
        if model_pass2 != model_pass:
            grabar = User(id=user.id, username=user.username, email=user.email,
                          password=model_pass2)
            if (model_pass2 == model_pass3):
                grabar.save()
                user = User.objects.get(id=current_user.id)
                user.is_staff = True
                user.is_active = True
                user.set_password(user.password)
                user.save()
                username = user.username
                password = model_pass2
                user = authenticate(
                    request, username=username, password=password)
                if user:
                    login(request, user)
                    return mostrar_notas(request)
            else:
                print("contraseña no coincide")
                return redirect('changePass')
        else:
            print("formulario invalido")
            return redirect('changePass')
    else:
        newUser = changePassForm()
    return render(request, "login/changePass.html", {'User': newUser})
