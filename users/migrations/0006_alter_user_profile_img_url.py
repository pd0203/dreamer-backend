# Generated by Django 4.0.6 on 2022-10-31 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_country_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img_url',
            field=models.URLField(null=True),
        ),
    ]
