# Generated by Django 4.0.2 on 2022-12-23 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recipian',
            new_name='recipient',
        ),
    ]