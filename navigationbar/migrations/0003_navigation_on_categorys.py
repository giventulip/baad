# Generated by Django 3.2 on 2021-04-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigationbar', '0002_navigation_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='on_categorys',
            field=models.BooleanField(default=False),
        ),
    ]