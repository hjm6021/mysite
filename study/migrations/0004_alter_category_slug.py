# Generated by Django 3.2 on 2021-05-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=50, unique=True, verbose_name='SLUG'),
        ),
    ]
