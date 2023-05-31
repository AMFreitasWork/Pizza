from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'pizza/home.html')

def order(request):
    return render (request, 'pizza/order.html')

def story (request):
    return render (request, 'pizza/story.html')

def Promocao(request):
    return render (request, 'pizza/promocao.html')

def pizza(request):
    return render (request, 'pizza/pizza.html')

def Message(request):
    return render (request, 'pizza/message.html')

def Perguntas(request):
    return render (request, 'pizza/perguntas.html')

def Reclamacao(request):
    return render (request, 'pizza/reclamacao.html')

def Sugestao(request):
    return render (request, 'pizza/sugestao.html')