# Generated by Django 4.2 on 2023-05-18 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_first_name_userinfo_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column2',
            name='user',
        ),
        migrations.RemoveField(
            model_name='column3',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Column1',
        ),
        migrations.DeleteModel(
            name='Column2',
        ),
        migrations.DeleteModel(
            name='Column3',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
