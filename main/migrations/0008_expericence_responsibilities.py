# Generated by Django 5.2.4 on 2025-07-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_expericence'),
    ]

    operations = [
        migrations.AddField(
            model_name='expericence',
            name='responsibilities',
            field=models.TextField(default='Not mentioned'),
            preserve_default=False,
        ),
    ]
