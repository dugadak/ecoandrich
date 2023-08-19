# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Countries(models.Model):
    country_id = models.CharField(primary_key=True, max_length=2)
    country_name = models.CharField(max_length=40, blank=True, null=True)
    region = models.ForeignKey('Regions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=30)
    manager = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25)
    email = models.CharField(unique=True, max_length=25)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateTimeField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    commission_pct = models.DecimalField(max_digits=2, decimal_places=2, blank=True, null=True)
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class JobHistory(models.Model):
    employee = models.OneToOneField(Employees, models.DO_NOTHING, primary_key=True)  # The composite primary key (employee_id, start_date) found, that is not supported. The first column is selected.
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_history'
        unique_together = (('employee', 'start_date'),)


class Jobs(models.Model):
    job_id = models.CharField(primary_key=True, max_length=10)
    job_title = models.CharField(max_length=35)
    min_salary = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=25, blank=True, null=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'
