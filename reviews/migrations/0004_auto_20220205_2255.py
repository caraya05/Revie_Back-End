# Generated by Django 3.0 on 2022-02-06 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220205_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photorestaurant',
            name='photo_five',
        ),
        migrations.RemoveField(
            model_name='photorestaurant',
            name='photo_four',
        ),
        migrations.RemoveField(
            model_name='photorestaurant',
            name='photo_three',
        ),
        migrations.RemoveField(
            model_name='photorestaurant',
            name='photo_two',
        ),
        migrations.RemoveField(
            model_name='photoreview',
            name='photo_three',
        ),
        migrations.RemoveField(
            model_name='photoreview',
            name='photo_two',
        ),
    ]
