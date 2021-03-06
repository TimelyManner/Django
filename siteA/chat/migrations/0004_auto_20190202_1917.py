# Generated by Django 2.1.5 on 2019-02-02 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20190131_0917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='admin_id',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='owner',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='chat.User'),
        ),
    ]
