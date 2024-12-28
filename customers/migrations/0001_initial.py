# Generated by Django 5.1.3 on 2024-12-28 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]