# Generated by Django 2.2.5 on 2022-01-28 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0011_auto_20220128_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='imgtitle',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]