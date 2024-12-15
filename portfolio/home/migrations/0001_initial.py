# Generated by Django 5.1.4 on 2024-12-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('profile', models.ImageField(upload_to='profile/')),
                ('desc', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('github', models.CharField(max_length=1000)),
                ('linkdn', models.CharField(max_length=1000)),
                ('resume', models.FileField(upload_to='resume/')),
            ],
        ),
    ]