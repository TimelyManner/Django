# Generated by Django 2.1.5 on 2019-02-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20190202_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='admin_id',
            field=models.IntegerField(default=None),
        ),
    ]
