# Generated by Django 2.0 on 2018-10-09 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20181009_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]