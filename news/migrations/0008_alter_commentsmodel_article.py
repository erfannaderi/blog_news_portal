# Generated by Django 5.0.1 on 2024-01-07 21:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_commentsmodel_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.news'),
        ),
    ]