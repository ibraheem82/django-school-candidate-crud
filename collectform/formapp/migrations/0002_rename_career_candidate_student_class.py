# Generated by Django 4.1.1 on 2022-10-06 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='career',
            new_name='student_class',
        ),
    ]