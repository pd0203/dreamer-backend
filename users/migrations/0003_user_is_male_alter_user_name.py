# Generated by Django 4.0.6 on 2022-10-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_nofilter_highschool_rating_nofilter_highschool_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_male',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
