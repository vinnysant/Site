from django import forms
from Site.core.models import Funcionario


class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ('nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao')

    def __init__(self, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)

# class LoginForm (forms.Form):
    #usuario = forms.CharField(label="Usuario: ", max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    #senha = forms.CharField(label="Senha: ", widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    #def __init__(self, *args, **kwargs):
        #super(LoginForm, self).__init__(*args, **kwargs)
class FuncionarioUpdate(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ('nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao')

    def __init__(self, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)