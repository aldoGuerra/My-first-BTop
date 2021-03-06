# Generated by Django 3.0.4 on 2020-03-13 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=20)),
                ('talla', models.CharField(max_length=20)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuario_crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
