# Generated by Django 2.0 on 2018-10-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0026_auto_20181027_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspaper',
            name='is_ocr',
            field=models.BooleanField(default=False),
        ),
    ]
