# Generated by Django 2.2.1 on 2019-08-17 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0019_testcategory_center'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testcategory',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Test Categories'},
        ),
    ]