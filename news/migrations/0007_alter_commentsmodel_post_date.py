# Generated by Django 5.0.1 on 2024-01-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_commentsmodel_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
