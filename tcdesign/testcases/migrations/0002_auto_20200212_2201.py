# Generated by Django 3.0.3 on 2020-02-12 21:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testcases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]