# Generated by Django 2.2 on 2019-06-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20190606_1910'),
        ('accounts', '0004_auto_20190605_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ratings',
            field=models.ManyToManyField(through='accounts.Rating', to='main_app.Recipe'),
        ),
    ]