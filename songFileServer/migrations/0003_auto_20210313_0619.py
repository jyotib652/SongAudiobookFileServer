# Generated by Django 3.1.7 on 2021-03-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songFileServer', '0002_auto_20210313_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='name',
        ),
        migrations.AlterField(
            model_name='podcast',
            name='podcastParticipants',
            field=models.CharField(choices=[], max_length=100, null=True),
        ),
    ]
