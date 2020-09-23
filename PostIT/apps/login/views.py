from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.urls import *
#from django.contrib import messages
from apps.user.views import mostrar_notas
from apps.user.models import *
from apps.user.forms import *

# Create your views here.

#from django.contrib.auth.forms import UserCreationForm


def index(request):
    # login
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
                valor = current_user
                user = User.objects.get(username=model_username)
                return mostrar_notas(request, user)
            else:
                #messages.success(request, 'data error :')
                return redirect('index')
    newUser = registerUser(request.POST)  # crear usuario
    model = User
    if newUser.is_valid():
        model.username = newUser.cleaned_data["username"]
        model.email = newUser.cleaned_data["email"]
        model.password1 = newUser.cleaned_data["password1"]
        model.password2 = newUser.cleaned_data["password2"]
        grabar = User(username=model.username, email=model.email,
                      password=model.password1)  # instanciar el modelo
        if (model.password1 == model.password2):
            grabar.save()
            user = User.objects.get(username=model.username)
            user.is_staff = True
            user.is_active = True
            user.save()
            # >>> from django.contrib.auth.models import User
            u = User.objects.get(username=model.username)
            u.set_password(model.password1)
            u.save()
            #messages.success(request, 'New user create whit name '+model.username)
            return redirect('index')
    else:
        newUser = registerUser()
        log_in = LoginForm()
    return render(request, 'login/index.html', {'newUser': newUser, "log_in": log_in})


@login_required
def logout(request):
    logout(request)
    return('index')


'''
class RegistroUsuario(CreateView):
   model = User
   template_name = "registrar.html"
   form_class = forms.RegistrationForm
   succes_url = reverse_lazy('listausers')

   def form_valid(self, form):
    self.object.groups.clear()
    self.object.groups.add(form.cleaned_data['group'])
    return super(RegistroUsuario, self).form_valid(form)'''
