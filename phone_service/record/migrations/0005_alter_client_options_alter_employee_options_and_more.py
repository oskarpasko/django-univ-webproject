# Generated by Django 4.2.1 on 2023-06-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_alter_service_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'Client'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': 'Employee'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name_plural': 'Location'},
        ),
        migrations.AlterModelOptions(
            name='posn',
            options={'verbose_name_plural': 'Position'},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name_plural': 'Record'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': 'Service'},
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(default='Vancouver', max_length=255),
        ),
    ]
