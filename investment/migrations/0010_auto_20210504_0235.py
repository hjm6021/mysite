# Generated by Django 3.2 on 2021-05-04 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0009_auto_20210504_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
