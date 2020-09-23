from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import registernota

# Create your views here.

# fuciona creando notas de id_usuario=1 y con el usuario de id=1


@login_required
def mostrar_notas(request, user):
    try:
        todos = nota.objects.filter(id_usuario=user.id).order_by("fecha")
    except:
        todos: ""
    ctx = {"user": user, "notas": todos}
    return render(request, "home/notas.html", ctx)


@login_required
def edit(request):
    print(nota.id)
    ctx = {}
    return render(request, "home/edit.html", ctx)


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
            grabar = nota(id_usuario=user, titulo=model.titulo, fecha=model.fecha,
                          descripcion=model.descripcion, color=model.color)
            grabar.save()
            return mostrar_notas(request, user)
        else:
            return redirect('home')
    else:
        newnote = registernota()
    return render(request, "home/create.html", {"newnote": newnote})
