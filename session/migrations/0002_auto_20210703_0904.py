# Generated by Django 3.2.4 on 2021-07-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='session',
            name='jornal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Report_Session',
        ),
    ]