# Generated by Django 2.0 on 2018-10-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20181009_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='file',
            field=models.FileField(unique=True, upload_to='', verbose_name='pdfs/'),
        ),
    ]