from django import forms
from .models import Autor
from .models import Avaliador
from .models import EnviarProjeto
from .models import AvaliarProjeto
from .models import Premio


# creating a form
class AutorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Autor

        # specify fields to be used
        fields = [
            "nome",
            "cpf",
            "telefone",
            "endereco"

        ]

class AvaliadorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Avaliador

        # specify fields to be used
        fields = [
            "nome",
            "cpf",
            "telefone",
            "endereco"

        ]

class   EnviarProjetoForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = EnviarProjeto

        # specify fields to be used
        fields = [
            "area",
            "titulo",
            "resumo",
            "dataEnvio"

        ]
class   AvaliarProjetoForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = AvaliarProjeto

        # specify fields to be used
        fields = [
            "avaliador",
            "parecer",
            "nota",
            "dataAvaliacao"

        ]

class   PremioForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Premio

        # specify fields to be used
        fields = [
            "nome",
            "descricao",
            "cronograma",
            "autor"

        ]