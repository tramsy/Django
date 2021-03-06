# Generated by Django 3.2.7 on 2022-06-09 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pradigm', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageInventor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('language', models.ManyToManyField(to='laguages.Language')),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='inventor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laguages.languageinventor'),
        ),
    ]
