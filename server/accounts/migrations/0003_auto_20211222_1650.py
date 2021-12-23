# Generated by Django 3.2.10 on 2021-12-22 07:50

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211219_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=12, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]