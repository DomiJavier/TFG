# Generated by Django 3.2.9 on 2021-11-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0003_auto_20211121_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='start',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='evento',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
