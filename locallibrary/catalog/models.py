from django.db import models


class Autor(models.Model):

    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Auxiliar(models.Model):

    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class EnviarProjeto(models.Model):

    area = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    resumo = models.CharField(max_length=250)
    autores = models.ManyToManyField(Autor)
    dataEnvio = models.DateField(null=False)

    def __str__(self):
        return self.titulo


class Avaliador(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class AvaliarProjeto(models.Model):

    avaliador = models.ForeignKey(Avaliador,models.CASCADE, verbose_name="Avaliador")
    parecer = models.CharField(max_length=50)
    nota = models.DecimalField(max_digits=4,decimal_places=2)
    dataAvaliacao = models.DateField(null=False)


class Premio(models.Model):

    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50,)
    cronograma= models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)

    def __str__(self):
         return self.nome