# Generated by Django 5.0 on 2023-12-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('model', models.CharField(max_length=40)),
                ('engine', models.CharField(max_length=40)),
                ('power', models.CharField(max_length=40)),
            ],
        ),
    ]
