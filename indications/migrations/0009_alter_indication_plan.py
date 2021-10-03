# Generated by Django 3.2.4 on 2021-10-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indications', '0008_alter_indication_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indication',
            name='plan',
            field=models.CharField(choices=[('Standard', 'Standard'), ('Basic', 'Basic'), ('Premium', 'Premium'), ('Free', 'Free')], default='Free', max_length=10),
        ),
    ]