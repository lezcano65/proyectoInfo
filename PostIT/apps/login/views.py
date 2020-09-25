from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
#from django.contrib import messages

from apps.user.views import mostrar_notas
from apps.user.models import nota
from apps.user.forms import registerUser, LoginForm, registernota


# Create your views here.


def indexPage(request):
    if request.method == "POST":
        log_in = LoginForm(request.POST)
        model_username = request.POST.get('username')
        model_password = request.POST.get('password')
        if (model_username != None) and (model_password != None):
            if log_in.is_valid():
                user = authenticate(username=model_username,
                                    password=model_password)
                #messages.success(request, 'User name is: '+model_username)
                login(request, user)
                current_user = request.user
                print(current_user.id)
                user = User.objects.get(username=model_username)
                return mostrar_notas(request)
            else:
                #messages.success(request, 'data error :')
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
            #messages.success(request, 'New user create whit name '+model.username)
            return redirect('index')
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
    print(current_user.id)
    ctx = {}
    return render(request, 'login/settings.html', ctx)


@login_required  # permiso para usuario
def changeEmail(request):
    if request.method == "POST":  # post input para views
        current_user = request.user  # instanciando el usurio logueado
        # busqueda a la base de datos del usuario
        user = User.objects.get(id=current_user.id)
        print(user.id)
        newUser = changeEmail(request.POST)  # instanciar el formulario
        model = User  # instanciar el modelo de User
        if newUser.is_valid():
            model.username = user.username
            model.email = newUser.cleaned_data["email"]
            model.email1 = newUser.cleaned_data["email1"]
            model.email2 = newUser.cleaned_data["email2"]
            model.password = newUser.cleaned_data["password"]
            grabar = User(id=user.id, username=model.username, email=model.email,
                          password=model.password)
            if (model.email1 == model.email2):
                grabar.save() #

    else:
        newUser = changeEmail()
    return render(request, 'login/changeEmail.html', {})


@login_required
def changeUsername(request):
    pass
    return redirect()


@login_required
def changePass(request):
    return render(request, 'login/changePass.html', {})
