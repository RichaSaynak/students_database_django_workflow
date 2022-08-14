from rest_framework import serializers
from .models import Attendance
from students.models import Student , Grade


from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_name')



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'student_name', 'student_address', 'student_email', 'student_account')




class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        # fields = ('id', 'student', 'course', 'grade_received')
        fields = ('id','student', 'course', 'grade_received')
        # fields = ('grade_received',)



class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        # fields = ('id', 'student', 'course', 'grade_received')
        fields = ('id','student', 'course', 'date_of_attendance','attended_question')
        # fields = ('grade_received',)




# class StudentSerializer(serializers.ModelSerializer):
#     # course = CourseSerializer(read_only=True, many=True)
#     courses = GradeSerializer(read_only=True, many=True)
#     class Meta:
#         model = Student
#         fields = ('id', 'student_name', 'student_address', 'student_email', 'courses','student_account')












