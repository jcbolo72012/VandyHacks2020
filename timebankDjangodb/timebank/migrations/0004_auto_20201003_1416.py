# Generated by Django 3.1.2 on 2020-10-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timebank', '0003_auto_20201003_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='credits',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
