from django.shortcuts import render

# Create your views here.
def v_list(request):
    context = {}
    return render(request, 'list.html', context)

def v_create(request):
    context = {}
    return render(request, 'create.html', context)

def v_update(request):
    context = {}
    return render(request, 'update.html', context)

def v_delete(request):
    context = {}
    return render(request, 'delete.html', context)




