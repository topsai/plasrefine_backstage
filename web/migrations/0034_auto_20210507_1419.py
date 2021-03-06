# Generated by Django 3.2 on 2021-05-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_alter_websetting_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'COMMUNITY/FAQS', 'verbose_name_plural': 'COMMUNITY/FAQS'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='introduction',
            field=models.CharField(max_length=300, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
