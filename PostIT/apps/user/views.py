from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import registernota, registerUser
from .models import nota
from .filters import notaFilter

# Create your views here.


@login_required
def mostrar_notas(request):
    try:
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        todos = nota.objects.filter(id_usuario=user.id).order_by("fecha")
        print("paso 1")
        MyFilter = notaFilter(request.GET, queryset=todos)
        print("paso 2")
        todos = MyFilter.qs
        print("paso 3")
    except:
        todos: ""

    ctx = {"user": user, "notas": todos, "filtro": MyFilter}
    return render(request, "home/notas.html", ctx)


@login_required
def edit(request, notuli):
    print(notuli.id)
    ctx = {}
    return render(request, "home/edit.html", ctx)


@login_required
def deleteNote(request, notuli):
    print(notuli.id)
    ctx = {}
    return render(request, "home/notas.html", ctx)


@login_required
def newnota(request):
    if request.method == "POST":
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        newnote = registernota(request.POST)
        model = nota
        if newnote.is_valid():
            model.titulo = newnote.cleaned_data["titulo"]
            model.descripcion = newnote.cleaned_data["descripcion"]
            model.fecha = newnote.cleaned_data["fecha"]
            model.color = newnote.cleaned_data["color"]
            grabar = nota(id_usuario=user, titulo=model.titulo, check=True, fecha=model.fecha,
                          descripcion=model.descripcion, color=model.color)
            grabar.save()
            return mostrar_notas(request, user)
        else:
            return redirect('home')
    else:
        newnote = registernota()
    return render(request, "home/create.html", {"newnote": newnote})


@login_required
def searchNote(request):
    current_user = request.user
    print(current_user.id)
    buscale = request.Search
    print(buscale)
    if buscale != None:
        print(buscale)
        notuli = nota.objects.filter(titulo=buscale)
        ctx = {"user": current_user, "notas": notuli}
        return render(request, "home/notas.html", ctx)
    return render(request, "home/notas.html", ctx)


@login_required
def configuracion(request):
    if request.method == "POST":
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        print(user.id)
        newUser = registerUser(request.POST)
        model = User
        if newUser.is_valid():
            model.username = newUser.cleaned_data["username"]
            model.email = newUser.cleaned_data["email"]
            model.password1 = newUser.cleaned_data["password1"]
            model.password2 = newUser.cleaned_data["password2"]
            grabar = User(id=user.id, username=model.username, email=model.email,
                          password=model.password1)
            if (model.password1 == model.password2):
                grabar.save()
                user = User.objects.get(username=model.username)
                user.is_staff = True
                user.is_active = True
                user.set_password(model.password1)
                user.save()
                return mostrar_notas(request, user)
            else:
                print("contraseña no coincide")
        else:
            print("formulario invalido")
    else:
        newUser = registerUser()
    return render(request, "home/settings.html", {'User': newUser})


@login_required
def informatorio(request):

    return render(request, "home/informatorio.html", {})
