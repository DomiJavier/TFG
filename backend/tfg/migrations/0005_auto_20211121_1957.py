# Generated by Django 3.2.9 on 2021-11-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tfg', '0004_auto_20211121_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='start',
            field=models.CharField(max_length=10),
        ),
    ]
