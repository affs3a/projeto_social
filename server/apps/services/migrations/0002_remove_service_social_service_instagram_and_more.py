# Generated by Django 4.2.5 on 2024-01-03 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='social',
        ),
        migrations.AddField(
            model_name='service',
            name='instagram',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='service',
            name='whatsapp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
