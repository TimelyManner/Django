# Generated by Django 2.1.5 on 2019-01-31 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No Title', max_length=20)),
                ('admin_id', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='Anonymous', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='chatroom',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.User'),
        ),
    ]
