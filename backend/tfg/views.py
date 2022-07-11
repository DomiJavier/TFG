from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from tfg.models import *
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import get_messages
from urllib import request
# Create your views here.

def funciona(request): #primera vista
    return HttpResponse("Funciona")

def login(request): #login
    form = UserCreationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['usuario']
        message.success(request, f'Usuario {usuario} creado')
    context = {'form' : form}
    return render(request, 'login.html', context)
@login_required
def calendario(request): #calendario full calendar
    context = {
        "eventos": Evento.objects.all()
    }
    return render(request, 'calendario.html', context)
def evento(request):
    if request.method == 'POST':
        title = request.POST['title']
        start = request.POST['start']
        lugar = request.POST['lugar']
        nuevo = Evento(title=title,start=start,lugar=lugar)
        nuevo.save()
        datos = {
                'title': title,
                'start': start
            }
        return JsonResponse(datos)
def salir(request):
    logout(request)
    return redirect('/')
def crearDatos(request):
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2018-01-01T00:00:00UTC/fechafin/2021-01-10T00:00:00UTC/estacion/3129/?api_key=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJkb21pOTVAaG90bWFpbC5lcyIsImp0aSI6ImJiNzM0Mzg2LWUwYjEtNDZlMy04YTgxLTBkMTFjYWVmMjQwMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjM1NTEyMzk5LCJ1c2VySWQiOiJiYjczNDM4Ni1lMGIxLTQ2ZTMtOGE4MS0wZDExY2FlZjI0MDMiLCJyb2xlIjoiIn0.rjTXU1Jnu52ELvvUGDHF9FXZSewZa5B3P0RQKDDlju8"
    result = request.post(url)
    print(result.url)
    print(result)

def registro(request):
    context = {}
    return render(request, 'registro.html', context)
def registrar(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    if (User.objects.filter(username=username).exists()):
        context = {
                'existe': 'existe',
            }
        return render(request, 'registro.html', context)
    else:
        User.objects.create_user(username=username, password=password)
        return redirect('/')
def perfil(request):
    user = request.user.username
    context = {'username': user}
    return render(request, 'perfil.html', context)
def perfilM(request):
    instance = request.user.id
    if request.method == 'POST':
        password = request.POST['password']
        hashed_pwd = make_password(password)
        User.objects.update(password=hashed_pwd)
        messages.success(request,"Se ha cambiado la contraseña, vuelva a acceder.")
    return redirect('login')
