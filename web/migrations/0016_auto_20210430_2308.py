# Generated by Django 3.2 on 2021-04-30 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_richtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='websetting',
            name='SettingName',
            field=models.CharField(default=1, max_length=60, verbose_name='配置名称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='websetting',
            name='about',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about', to='web.richtext', verbose_name='关于我们'),
        ),
    ]
