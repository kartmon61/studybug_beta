# Generated by Django 2.2.7 on 2019-11-15 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='licences',
        ),
        migrations.AddField(
            model_name='license',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
