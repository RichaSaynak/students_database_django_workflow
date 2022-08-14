from rest_framework import serializers
from student_accounts.models import Student_Account


class Student_AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Account
        fields = ('id', 'username', 'password')




class Student_AccountSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Student_Account
        fields = ('id', 'username')
