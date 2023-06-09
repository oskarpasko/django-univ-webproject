# Generated by Django 4.0.2 on 2023-05-30 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='record.location'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='posn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.posn'),
        ),
        migrations.AlterField(
            model_name='record',
            name='client',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='record',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.location'),
        ),
        migrations.AlterField(
            model_name='record',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='record.service'),
        ),
    ]
