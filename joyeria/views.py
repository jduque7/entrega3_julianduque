from django.shortcuts import render, redirect
from .models import Categoria, Material, Joya
from .forms import CategoriaForm, MaterialForm, JoyaForm 

def home(request):
    return render(request, 'joyeria/home.html')



def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('home') 
    else:
        form = CategoriaForm() 
    
    return render(request, 'joyeria/formulario_generico.html', {'form': form, 'titulo': 'Nueva Categoría'})

def agregar_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MaterialForm()
    
    return render(request, 'joyeria/formulario_generico.html', {'form': form, 'titulo': 'Nuevo Material'})

def agregar_joya(request):
    if request.method == 'POST':
        form = JoyaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JoyaForm()
    
    return render(request, 'joyeria/formulario_generico.html', {'form': form, 'titulo': 'Nueva Joya'})
def buscar(request):
    query = request.GET.get('q', '') 
    
    if query:
        
        data = Joya.objects.filter(nombre__icontains=query)
    else:
        data = []

    return render(request, 'joyeria/buscar.html', {'data': data, 'query': query})