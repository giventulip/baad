# Generated by Django 3.2 on 2021-04-22 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('navigationbar', '0003_navigation_on_categorys'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryByNav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('link', models.TextField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navigationbar.navigation')),
            ],
        ),
    ]
