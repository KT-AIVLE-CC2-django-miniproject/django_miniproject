# Generated by Django 2.2.5 on 2022-01-28 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0008_auto_20220128_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
