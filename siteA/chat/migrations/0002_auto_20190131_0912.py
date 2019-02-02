# Generated by Django 2.1.5 on 2019-01-31 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='Anonymous', max_length=20, primary_key=True, serialize=False),
        ),
    ]