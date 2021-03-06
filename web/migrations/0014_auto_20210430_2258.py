# Generated by Django 3.2 on 2021-04-30 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_image_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': '图片', 'verbose_name_plural': '图片'},
        ),
        migrations.AlterField(
            model_name='websetting',
            name='about',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about', to='web.text', verbose_name='关于我们'),
        ),
        migrations.AlterField(
            model_name='websetting',
            name='title',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='title', to='web.text', verbose_name='网站名称'),
        ),
    ]
