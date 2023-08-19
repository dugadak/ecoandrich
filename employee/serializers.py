# serializers.py
from rest_framework import serializers
from .models import Employees, JobHistory, Departments, Locations, Countries, Regions

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        
class JobHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobHistory
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'