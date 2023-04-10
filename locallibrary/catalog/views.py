from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Autor, Avaliador, EnviarProjeto, AvaliarProjeto, Premio
from .forms import AutorForm, AvaliadorForm, EnviarProjetoForm, AvaliarProjetoForm, PremioForm


def list_autor_view(request):

    autor = Autor.objects.all()
    context = {}
    context["object_list"] = autor

    # add the dictionary during initialization
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "autores/list_autores.html", context)


def novo_autor_view(request):
    if request.method=='POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("index")
            except:
                pass
    else:
        form = AutorForm

    return render(request, "autores/novo_autor.html", {'form':form})


# update view for details
def editar_autor_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Autor, id=id)

    # pass the object as instance in form
    form = AutorForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "autores/editar_autor.html", context)


# delete view for details
def delete_autor_view(request, id):
    # dictionary for initial data with
    # field names as keys

    # fetch the object related to passed id
    autor=Autor.objects.get(id=id)

    autor.delete()
    # after deleting redirect to
    # home page
    return HttpResponseRedirect("/")




def novo_avaliador_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = AvaliadorForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "novo_avaliador_view.html", context)



def novo_Projeto_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = EnviarProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "novo_Projeto_view.html", context)

def inserir_nota_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = AvaliarProjetoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "inserir_nota_view.html", context)

def inserir_premio_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = PremioForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "inserir_premio_view.html", context)




def listar_avaliador_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Avaliador.objects.get(id=id)

    return render(request, "listar_avaliador_view", context)

def listar_projetos_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = EnviarProjeto.objects.get(id=id)

    return render(request, "listar_projetos_view", context)

def listar_notas_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = AvaliarProjeto.objects.get(id=id)

    return render(request, "listar_notas_view", context)

def listar_premio_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Premio.objects.get(id=id)

    return render(request, "listar_premio_view", context)


# update view for details


def editar_avaliador_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Autor, id=id)

    # pass the object as instance in form
    form = AvaliadorForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "editar_avaliador.html", context)

def editar_projeto_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Autor, id=id)

    # pass the object as instance in form
    form = EnviarProjetoForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "editar_projeto.html", context)

def editar_nota_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(AvaliarProjeto, id=id)

    # pass the object as instance in form
    form = AvaliarProjetoForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "editar_nota.html", context)

def editar_premio_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Premio, id=id)

    # pass the object as instance in form
    form = PremioForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "editar_premio.html", context)



def delete_avaliador_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Avaliador, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_avaliador_view.html", context)

def delete_projeto_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(EnviarProjeto, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_projeto_view.html", context)

def delete_nota_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(AvaliarProjeto, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_nota_view.html", context)

def delete_premio_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Premio, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_premio_view.html", context)