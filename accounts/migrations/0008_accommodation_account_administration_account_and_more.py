# Generated by Django 5.1.7 on 2025-04-09 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_contact_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
        migrations.AddField(
            model_name='administration',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
        migrations.AddField(
            model_name='bank',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
