# Generated by Django 2.0 on 2018-10-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20181009_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspaper',
            name='is_processed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
