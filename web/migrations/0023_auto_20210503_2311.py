# Generated by Django 3.2 on 2021-05-03 15:11

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_auto_20210503_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('img', imagekit.models.fields.ProcessedImageField(upload_to='DF_goods/Image/%Y/%m', verbose_name='图片')),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contact',
            },
        ),
        migrations.AlterModelOptions(
            name='indexpage',
            options={'verbose_name': 'Home', 'verbose_name_plural': 'Home'},
        ),
    ]