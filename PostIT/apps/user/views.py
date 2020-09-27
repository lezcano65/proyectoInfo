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
        MyFilter = notaFilter(request.GET, queryset=todos)
        todos = MyFilter.qs
    except:
        todos: ""
    ctx = {"user": user, "notas": todos, "filtro": MyFilter}
    return render(request, "home/notas.html", ctx)


@login_required
def edit(request, pk):
    print(pk)
    buscar = nota.objects.get(id=pk)
    print("antes del post")
    if request.method == "POST":
        print("post")
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        newnote = registernota(request.POST)
        model = nota
        if newnote.is_valid():
            print("entro")
            model.titulo = newnote.cleaned_data["titulo"]
            model.descripcion = newnote.cleaned_data["descripcion"]
            model.fecha = newnote.cleaned_data["fecha"]
            model.color = newnote.cleaned_data["color"]
            grabar = nota(id=buscar.id, id_usuario=user, titulo=model.titulo, fecha=model.fecha,
                          descripcion=model.descripcion, color=model.color)
            grabar.save()
            return mostrar_notas(request)
        else:
            return redirect('edit/',pk)
    else:
        print("enviar formulario")
        newnote = registernota(instance=buscar)
    return render(request, "home/edit.html", {"nota": newnote})


@login_required
def deleteNote(request, pk):
    buscar = nota.objects.get(id=pk)
    if request.method == "POST":
        grabar = nota(id=buscar.id, id_usuario=buscar.id_usuario, titulo=buscar.titulo, fecha=buscar.fecha,
                      descripcion=buscar.descripcion, color=buscar.color)
        grabar.delete()
        return mostrar_notas(request)
    else:
        print("enviar formulario")
        newnote = registernota(instance=buscar)
    return render(request, "home/delete.html", {"nota": newnote})


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
            return mostrar_notas(request)
        else:
            return redirect('home', {"newnote": newnote})
    else:
        newnote = registernota()
    return render(request, 'home/create.html', {"newnote": newnote})


@login_required
def searchNote(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    buscale = request.Search
    if buscale != None:
        notuli = nota.objects.filter(titulo=buscale)
        ctx = {"user": current_user, "notas": notuli}
        return render(request, "home/notas.html", ctx)
    else:
        ctx = {"user": current_user, "notas": notuli}
    return mostrar_notas(request)


@login_required
def informatorio(request):

    return render(request, "home/informatorio.html", {})
