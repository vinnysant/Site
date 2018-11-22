from django.shortcuts import render
from Site.core.models import Funcionario
from Site.core.forms import FuncionarioForm

# Create your views here.
def Home (request):

    funcionario = Funcionario.objects.all()
    form = FuncionarioForm()

    if request.method == 'POST':
        # cria uma instancia do formulario com os dados vindos do request POST:
        form = FuncionarioForm(data=request.POST or None)
        # Checa se os dados são válidos:
        if form.is_valid():
            msg = "Cadastro realizado com sucesso"
            # Caso o login seja concluído, redireciona para a HOME:
            form.save()

    return render(request, 'index.html', {'funcionario': funcionario, 'formulario': form})