from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerializers, EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    # URL: companies/{company_id}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            employees_serializer = EmployeeSerializers(employees, many=True, context={'request': request})
            return Response(employees_serializer.data)
        except Exception as ex:
            print(f"Exception: {ex}")
            return Response({
                'message': 'Company Does Not Exist !!'
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    