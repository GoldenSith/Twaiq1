# Generated by Django 5.0 on 2023-12-08 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Username', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('Password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(max_length=255)),
                ('Content', models.CharField(max_length=255)),
                ('Category', models.CharField(max_length=255)),
                ('Date_published', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Content', models.CharField(max_length=255)),
                ('Date_posted', models.DateField()),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.member')),
                ('Post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]