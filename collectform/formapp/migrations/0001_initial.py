# Generated by Django 4.1.1 on 2022-10-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=120)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True)),
                ('career', models.CharField(choices=[('JSS 1', 'JSS 1'), ('JSS 2', 'JSS 2'), ('JSS 3', 'JSS 3'), ('SSS 1', 'SSS 1'), ('SSS 2', 'SSS 2'), ('SSS 3', 'SSS 3')], max_length=80, null=True)),
            ],
        ),
    ]
