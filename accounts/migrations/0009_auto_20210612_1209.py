# Generated by Django 3.1.6 on 2021-06-12 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210611_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirmpassword',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fullname',
        ),
    ]