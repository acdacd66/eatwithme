# Generated by Django 3.0.6 on 2020-05-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='writer',
            field=models.CharField(max_length=500, null=True),
        ),
    ]