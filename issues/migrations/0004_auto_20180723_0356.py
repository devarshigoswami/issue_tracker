# Generated by Django 2.0.7 on 2018-07-23 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_auto_20180723_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_assignee', to=settings.AUTH_USER_MODEL),
        ),
    ]
