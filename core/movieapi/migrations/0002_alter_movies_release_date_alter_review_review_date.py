# Generated by Django 5.0 on 2023-12-23 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
