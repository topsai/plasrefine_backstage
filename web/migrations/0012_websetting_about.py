# Generated by Django 3.2 on 2021-04-30 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_text_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='websetting',
            name='about',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.image', verbose_name='关于我们'),
            preserve_default=False,
        ),
    ]
