# Generated by Django 3.1.1 on 2020-12-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0008_tourimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.CharField(max_length=15)),
                ('adult', models.CharField(max_length=3)),
                ('children', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='tours',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
