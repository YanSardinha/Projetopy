from django.urls import path
from .views import novo_autor_view

urlpatterns = [
        path("", novo_autor_view)

]