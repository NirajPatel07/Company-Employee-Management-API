from django.contrib import admin
from companyApi.models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'company')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company, CompanyAdmin)
