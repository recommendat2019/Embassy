# Generated by Django 2.2.4 on 2019-11-21 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(null = True,on_delete=django.db.models.deletion.DO_NOTHING, related_name='id+', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
