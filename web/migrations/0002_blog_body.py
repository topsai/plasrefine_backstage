# Generated by Django 3.2 on 2021-04-29 15:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
