# Generated by Django 4.2.4 on 2023-08-17 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('country_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('hire_date', models.DateTimeField()),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('commission_pct', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=35)),
                ('min_salary', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('max_salary', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
            ],
            options={
                'db_table': 'jobs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(blank=True, max_length=40, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=12, null=True)),
                ('city', models.CharField(max_length=30)),
                ('state_province', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'locations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'regions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='employee.employees')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'job_history',
                'managed': False,
            },
        ),
    ]
