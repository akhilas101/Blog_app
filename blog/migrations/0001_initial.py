# Generated by Django 4.1.13 on 2023-11-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(default='', max_length=100)),
                ('title', models.CharField(default='', max_length=100)),
                ('message', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
