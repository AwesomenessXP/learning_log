# Generated by Django 4.0.6 on 2022-07-22 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_rename_topping_pizza'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza',
            new_name='pizzeria',
        ),
    ]