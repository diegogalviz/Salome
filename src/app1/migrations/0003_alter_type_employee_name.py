# Generated by Django 4.2.1 on 2023-05-20 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_type_employeed_type_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type_employee',
            name='name',
            field=models.CharField(max_length=150, verbose_name='nombre_tipo'),
        ),
    ]
