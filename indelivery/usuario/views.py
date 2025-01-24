from django.shortcuts import render, redirect # Para redirecionar o usuario
from django.http import HttpResponse, HttpRequest
from hashlib import sha256 # Criptografar a senha
from .models import Usuario


# Create your views here.

def home(requests):
    return render(requests, 'home.html', {'nome' : 'Franch'})

def cadastrar(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'cadastro.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        usuario_banco = Usuario.objects.filter(nome=username)
        if len(usuario_banco) > 0:
            return redirect('/cadastro?status=1')
        
        if len(password) < 8:
            return redirect('/cadastro?status=2')
        
        try:
            password = sha256(password.encode()).hexdigest()
            usuario = Usuario(
                nome = username,
                senha = password,
                email = email
            )
            usuario.save()
            return redirect('/login')
        except:
            return redirect('/cadastro')
    
def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST['username']
        password = request.POST['password']
        
        password = sha256(password.encode()).hexdigest()

        usuario = Usuario.objects.filter(nome=user).filter(senha=password)

        if len(usuario) == 0:
            return redirect('/login')
        elif len(usuario) > 0:
            request.session['usuario'] = usuario[0].id
            return redirect('/')
        

def logout(request: HttpRequest) -> HttpResponse:
    request.session.flush()
    return redirect('/login')