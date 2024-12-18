# Generated by Django 3.0 on 2024-12-09 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0008_auto_20241209_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullload',
            name='paidAmt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remark', models.TextField()),
                ('date', models.DateField(null=True)),
                ('full_load', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balances', to='consign_app.Fullload')),
            ],
        ),
    ]
