# Generated by Django 5.1.2 on 2024-11-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_data_happiness_alter_journalentry_happiness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='happiness',
            field=models.IntegerField(),
        ),
    ]
