# Generated by Django 2.0 on 2018-10-01 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_tendersnippet_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tendersnippet',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tendersnippet',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Category'),
        ),
        migrations.AlterField(
            model_name='tendersnippet',
            name='finish_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='tendersnippet',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]
