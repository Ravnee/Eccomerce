# Generated by Django 4.0 on 2022-01-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_info',
            name='user_password',
            field=models.CharField(default='ravneet', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact_info',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
