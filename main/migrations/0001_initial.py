# Generated by Django 4.0.2 on 2022-02-07 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_genre', models.CharField(max_length=50)),
                ('movie_year', models.CharField(max_length=50)),
                ('movie_cast', models.CharField(max_length=500)),
                ('movie_image', models.ImageField(blank=True, upload_to='uploads')),
                ('site_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]