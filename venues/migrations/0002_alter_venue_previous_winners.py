# Generated by Django 4.0.3 on 2022-03-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='previous_winners',
            field=models.CharField(default=None, max_length=300),
        ),
    ]