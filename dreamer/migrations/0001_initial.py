# Generated by Django 4.0.6 on 2022-10-25 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DreamClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('avg_rating', models.FloatField()),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Dream_Classes',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Interests',
            },
        ),
        migrations.CreateModel(
            name='MBTI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'MBTIs',
            },
        ),
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamer.interest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User_Interests',
            },
        ),
        migrations.CreateModel(
            name='UserDreamClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dream_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamer.dreamclass')),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'User_Dream_Classes',
            },
        ),
        migrations.CreateModel(
            name='DreamClassReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('rating', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('dream_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamer.dreamclass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Dream_Class_Reviews',
            },
        ),
    ]
