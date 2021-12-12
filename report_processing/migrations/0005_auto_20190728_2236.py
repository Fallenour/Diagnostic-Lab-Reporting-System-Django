# Generated by Django 2.2.1 on 2019-07-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_processing', '0004_paymentvalidation_send_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentvalidation',
            name='send_message',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='paymentvalidation',
            name='upload_report',
            field=models.FileField(blank=True, null=True, upload_to='reports_PDF'),
        ),
    ]
