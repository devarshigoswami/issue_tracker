# Generated by Django 2.0.7 on 2018-07-24 02:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
