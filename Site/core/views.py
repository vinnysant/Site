from django.shortcuts import render

# Create your views here.
def Home (request):
    pessoas = {'pessoa':('Ricardo','rua 01','9999-9999'), 'carro':('Ford', '1.6', 'verde')}
    return render(request, 'index.html', pessoas)