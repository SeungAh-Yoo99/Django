# Generated by Django 3.1.5 on 2021-01-10 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_board_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='tags',
        ),
    ]
