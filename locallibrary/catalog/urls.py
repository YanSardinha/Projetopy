from django.urls import path
from .views import list_autor_view, novo_autor_view, editar_autor_view, delete_autor_view

urlpatterns = [
        path("", list_autor_view, name = 'index'),
        path("autor/create", novo_autor_view, name = 'novo_autor'),
        path("autor/edit/<int:id>", editar_autor_view, name = 'editar_autor'),
        path("autor/delete/<int:id>", delete_autor_view, name = 'delete_autor'),

]