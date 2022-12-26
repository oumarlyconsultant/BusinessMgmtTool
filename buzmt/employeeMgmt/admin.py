from django.contrib import admin
from .models import Country,City,Office,Department,Job,JobType,Employee,JobHistory,DepartmentHistory,EmploymentTerm,Schedule,WorkHour,SalaryPayment

# Register your models here.
# admin.site.register(Employee)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Office)
admin.site.register(Department)
admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(JobHistory)
admin.site.register(DepartmentHistory)
admin.site.register(EmploymentTerm)
admin.site.register(Schedule)
admin.site.register(WorkHour)
admin.site.register(SalaryPayment)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['lastName', 'firstName']
    # list_filter = ['startDate','endDate','activeInd']
    search_fields = ['lastName', 'firstName']
    ordering = ['lastName','firstName']

