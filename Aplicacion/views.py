from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CitaForm, CreateUserForm
from .filters import CitaFiltrar

# Create your views here.
def registerPage(request):
    form=CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'La cuenta fue creada para ' + user)

            return redirect('login')

    context = {'form':form}
    return render(request, 'Aplicacion/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username O Password incorrecto')
            

    context = {}
    return render(request, 'Aplicacion/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    citas = Cita.objects.all()
    pacientes = Paciente.objects.all()

    total_pacientes = pacientes.count()

    total_citas = citas.count()
    atendida=citas.filter(estado='Atendida').count()
    pendiente=citas.filter(estado='Pendiente').count()

    context = {'citas':citas, 'pacientes':pacientes, 'total_citas':total_citas, 'atendida':atendida, 'pendiente':pendiente}

    return render(request, 'Aplicacion/dashboard.html', context)

def products(request):
    especialidad = Especialidad.objects.all()

    return render(request, 'Aplicacion/products.html', {'especialidad':especialidad})

def registrarEspecialidad(request):
    nombre=request.POST['txtNombre']
    categoria=request.POST['txtCategoria']
    precio=request.POST['txtPrecio']

    especialidad = Especialidad.objects.create(nombre=nombre, categoria=categoria, precio=precio)

    especialidad = Especialidad.objects.all()
    return render(request, 'Aplicacion/products.html', {'especialidad':especialidad})

def pacienten(request):
    pacienten = Paciente.objects.all()

    return render(request, 'Aplicacion/pacienten.html', {'pacienten':pacienten})

def registrarPaciente(request):
    nombre=request.POST['txtNombre']
    celular=request.POST['txtCelular']
    email=request.POST['txtEmail']

    pacienten = Paciente.objects.create(nombre=nombre, celular=celular, email=email)

    pacienten = Paciente.objects.all()
    
    return render(request, 'Aplicacion/pacienten.html', {'pacienten':pacienten})

def customer(request, pk_test):
    paciente=Paciente.objects.get(id=pk_test)

    citas = paciente.cita_set.all()
    cita_count=citas.count()

    myfilter = CitaFiltrar(request.GET, queryset=citas)
    citas = myfilter.qs

    context={'paciente':paciente,'citas':citas, 'cita_count':cita_count, 'myfilter':myfilter}

    return render(request, 'Aplicacion/customer.html', context)

def crearCita(request):
    
    form=CitaForm()
    if request.method == 'POST':
        form=CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    return render(request, 'Aplicacion/cita_form.html', context)

def actualizarCita(request, pk):

    cita =Cita.objects.get(id=pk)
    form = CitaForm(instance=cita)

    if request.method =='POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, 'Aplicacion/cita_form.html', context)

def eliminarCita(request, pk):
    cita =Cita.objects.get(id=pk)
    if request.method =='POST':
        cita.delete() 
        return redirect('/')       
        

    context={'item':cita}
    return render(request, 'Aplicacion/delete.html', context)