# Generated by Django 3.2 on 2021-05-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0026_auto_20210504_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='contents',
            field=models.CharField(max_length=200, verbose_name='内容'),
        ),
    ]
