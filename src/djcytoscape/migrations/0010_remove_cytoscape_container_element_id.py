# Generated by Django 2.2.13 on 2020-07-06 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djcytoscape', '0009_auto_20200705_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cytoscape',
            name='container_element_id',
        ),
    ]