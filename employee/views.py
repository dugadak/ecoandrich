# views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Employees, JobHistory, Departments, Locations
from .serializers import EmployeeSerializer, JobHistorySerializer, DepartmentSerializer, LocationSerializer
from rest_framework.response import Response
from django.db.models import F

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    
    @action(detail=True, methods=['get'])
    def history(self, request,pk=None, *args, **kwargs):
        queryset = JobHistory.objects.filter(employee=pk)
        serializer = JobHistorySerializer(queryset, many=True)
        return Response({'History': serializer.data}, status=status.HTTP_200_OK)
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    
    @action(detail=True, methods=['patch'])
    def salary(self, request,pk=None, *args, **kwargs):
        percent = request.data.get('percent') / 100
        queryset = Employees.objects.filter(department_id=pk).update(salary=F('salary') * (1 + percent))
        return Response(f'해당 부서의 급여가 {int(percent*100)}% 적용되었습니다. 해당 부서의 사원 수 : {queryset}', status=status.HTTP_200_OK)
    
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer
    

    
