from django.shortcuts import render
from Site.core.models import Funcionario

# Create your views here.
def Home (request):
    funcionario = Funcionario.objects.all()

    return render(request, 'index.html', {'funcionario': funcionario, 'teste': '122334'})