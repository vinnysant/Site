from django.shortcuts import render
from Site.core.models import Funcionario
from Site.core.forms import FuncionarioForm

def Home (request):

    funcionario = Funcionario.objects.all()
    form = FuncionarioForm()

    if request.method == 'POST':
        form = FuncionarioForm(data=request.POST or None)
        if form.is_valid():
            form.save()

    return render(request, 'index.html', {'funcionario': funcionario, 'formulario': form})

def update (request, pk):
    data = {}
    funcionario = Funcionario.objects.get(pk=pk)
    form = FuncionarioForm(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()

    data['form'] = form
    return render(request, 'update.html', {'funcionario':funcionario, 'formulario':form}, data)