# model serializers
# regular serializers
from rest_framework import serializers
from dbapp.models import Employee,Department
from rest_framework.exceptions import ValidationError
class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'# manam ikkada emi papesethi outout data ave vasthave
class CustomSerializer(serializers.Serializer):
    empno = serializers.IntegerField()
    empname = serializers.CharField(max_length=20)
    salary = serializers.IntegerField()
    bonus = serializers.IntegerField()
    dept = serializers.IntegerField()

    def validate(self, attrs):
        if attrs['salary'] < 0:
            raise ValidationError({"salary": "salary cannot be negative"})
        return attrs
    def create(self, validated_data):
        dobj= Department.objects.get(deptno=validated_data['dept'])
        eobj=Employee.objects.create(empno=validated_data['empno'],
        empname=validated_data['empname'],
            salary=validated_data['salary']+validated_data['bonus'],
                dept=dobj)
        return eobj
    def update(self, instance, validated_data):
        dobj = Department.objects.get(deptno=validated_data['dept'])
        instance.empname=validated_data['empname']
        instance.salary=validated_data['salary']+validated_data['bonus']
        instance.dept=dobj
        instance.save()
        return instance
