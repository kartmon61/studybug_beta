# Generated by Django 2.2.1 on 2019-11-15 15:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_interest', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]