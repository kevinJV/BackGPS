# Generated by Django 2.1.5 on 2019-02-01 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Unidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidades',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
