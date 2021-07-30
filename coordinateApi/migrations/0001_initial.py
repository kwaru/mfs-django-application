# Generated by Django 3.2.5 on 2021-07-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_coordinate', models.CharField(max_length=1000000)),
                ('closet_paircoordinates', models.CharField(blank=True, editable=False, max_length=1000000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Coordinates',
                'ordering': ['-date_created'],
            },
        ),
    ]
