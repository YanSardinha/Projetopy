from django import forms
from .models import Autor, Avaliador, EnviarProjeto, AvaliarProjeto, Premio


# creating a form
class AutorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Autor

        # specify fields to be used
        fields = "__all__"


class AvaliadorForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Avaliador

        # specify fields to be used
        fields = "__all__"


class EnviarProjetoForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = EnviarProjeto

        # specify fields to be used
        fields = "__all__"


class AvaliarProjetoForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = AvaliarProjeto

        # specify fields to be used
        fields = "__all__"


class PremioForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Premio

        # specify fields to be used
        fields = "__all__"