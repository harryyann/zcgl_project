# Generated by Django 2.2.3 on 2019-12-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0007_remove_server_undernet'),
    ]

    operations = [
        migrations.AddField(
            model_name='servertype',
            name='modify_time',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]
