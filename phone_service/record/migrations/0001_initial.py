# Generated by Django 4.0.2 on 2023-05-30 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('street', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=5)),
                ('postcode', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=9, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posn',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('start_date', models.DateField()),
                ('deadline', models.DateField(blank=True, default=None, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('client', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.location')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.service')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=9)),
                ('location', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='record.location')),
                ('posn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.posn')),
            ],
        ),
    ]
