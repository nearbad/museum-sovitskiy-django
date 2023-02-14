# Generated by Django 4.1.6 on 2023-02-14 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='association',
        ),
        migrations.RemoveField(
            model_name='author',
            name='institution',
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exhibitions', to='main.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='exhibitionphoto',
            name='exhibition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='main.exhibition', verbose_name='Произведение'),
        ),
        migrations.AddField(
            model_name='author',
            name='association',
            field=models.ManyToManyField(blank=True, null=True, to='main.association', verbose_name='Группировка'),
        ),
        migrations.AddField(
            model_name='author',
            name='institution',
            field=models.ManyToManyField(blank=True, null=True, to='main.institution', verbose_name='Институция'),
        ),
    ]
