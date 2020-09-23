# Generated by Django 3.1 on 2020-09-22 23:33

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
            name='nota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.TextField(max_length=400)),
                ('fecha', models.DateField()),
                ('check', models.BooleanField(default=False, verbose_name='realizado')),
                ('color', models.CharField(max_length=60)),
                ('id_usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]