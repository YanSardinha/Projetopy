# Generated by Django 4.1.7 on 2023-04-04 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('endereco', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('endereco', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.IntegerField()),
                ('telefone', models.IntegerField()),
                ('endereco', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AvaliarProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paracer', models.CharField(max_length=50)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dataAvaliacao', models.DateField()),
                ('avaliador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.avaliador', verbose_name='Avaliador')),
            ],
        ),
        migrations.CreateModel(
            name='EnviarProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('resumo', models.CharField(max_length=250)),
                ('dataEnvio', models.DateField()),
                ('autores', models.ManyToManyField(to='catalog.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50)),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.autor')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]