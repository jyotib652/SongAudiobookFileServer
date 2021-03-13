# Generated by Django 3.1.7 on 2021-03-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songFileServer', '0009_auto_20210313_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='uploadedTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='uploadedTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='uploadedTime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
