from django.contrib import admin
from .models import Employee,Department

# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display=("empno","empname","salary","department","grade")
    list_editable=["empname"]
    list_filter=["salary"]
    def grade(self,obj):
        if obj.salary>200000:
            return 'High'
        elif obj.salary>150000:
            return 'Medium'
        else:
            return 'Low'
    def department(self,obj):
        return obj.dept.deptname if obj.dept else "No Dept"
    department.short_description = "Department"
    


admin.site.register(Employee,MyAdmin)
admin.site.register(Department)
