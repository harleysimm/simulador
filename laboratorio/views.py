from django.shortcuts import render
from .models import Laboratorio
from .forms import LaboratorioForm
from django.http import HttpResponseRedirect

# Create your views here.
def v_list(request):

    if 'numveces' in request.session:
        num = request.session["numveces"] #se obtiene la variable de sesion
    else:
        num = 0

    request.session['numveces'] = num + 1

    context = {
        "numveces": request.session["numveces"],
        "laboratorios": Laboratorio.objects.all()
    }

    return render(request, 'list.html', context)

def v_create(request):
    if request.method == 'POST':
        datos = request.POST.copy()
        formcrear = LaboratorioForm(datos)
        if formcrear.is_valid():
            formcrear.save()
        return HttpResponseRedirect("/")
    context = {
        'formulario': LaboratorioForm()
    }
    return render(request, 'create.html', context)

def v_update(request, laboratorio_id):
    lab = Laboratorio.objects.get(id = laboratorio_id)

    if request.method == 'POST':
        datos = request.POST.copy()
        formeditar = LaboratorioForm(datos, instance = lab)
        if formeditar.is_valid():
            formeditar.save()
        return HttpResponseRedirect('/')
    else:
        context = {
            'formedicion': LaboratorioForm(instance = lab)
        }
        return render(request, 'update.html', context)

def v_delete(request, laboratorio_id):
    if request.method == 'POST':
        from . models import Producto, DirectorGeneral
        Producto.objects.filter(laboratorio = laboratorio_id).delete()
        DirectorGeneral.objects.filter(laboratorio = laboratorio_id).delete()

        Laboratorio.objects.get(id = laboratorio_id).delete()
        return HttpResponseRedirect("/")

    context = {
        'lab': Laboratorio.objects.get(id = laboratorio_id) #capturando el laboratorio a eliminar
    }
    return render(request, 'delete.html', context)




