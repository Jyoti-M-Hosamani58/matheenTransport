# Generated by Django 3.0 on 2024-12-13 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0015_auto_20241210_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='full_load',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balances', to='consign_app.Fullload'),
        ),
    ]
