from django.shortcuts import render

from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from students.models import Student , Grade, Attendance
from students.serializers import StudentSerializer , GradeSerializer, AttendanceSerializer
from courses.models import Course
from django.http import Http404

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the students index.")



def index1(request):
    print("------------------------- I AM HERE")
    queryset = Student.objects.all()
    return render(request, "students/index.html", {'students': queryset})


class index1(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'students/index.html'

    def get(self, request):
        queryset = Student.objects.all()
        return Response({'students': queryset})




class list_all_students(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'students/student_list.html'

    def get(self, request):
        queryset = Student.objects.all()
        return Response({'students': queryset})




# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()

        name = request.GET.get('student_name', None)
        if name is not None:
            students = students.filter(student_name__icontains=name)

        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(student_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Student.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} students were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({'message': 'The student does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        student_serializer = StudentSerializer(student)
        return JsonResponse(student_serializer.data)

    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Student was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def student_list_address(request, address):
    students = Student.objects.filter(student_address=address)

    if request.method == 'GET':
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)



#-------------------------------------------------For Grades Table ----------------------------------------

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def grade_list(request):
    if request.method == 'GET':
        grades = Grade.objects.all()

        grade = request.GET.get('student', None)
        if grade is not None:
            grade = grades.filter(student_id__icontains=grade)

        grades_serializer = GradeSerializer(grades, many=True)
        return JsonResponse(grades_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        grade_data = JSONParser().parse(request)
        # print("grade_data",grade_data)
        # student = Student.objects.all()
        su = grade_data["student"]
        student = Student.objects.get(pk=su)
        # print("s1", student)
        da = grade_data["course"]
        course = Course.objects.get(pk=da)
        # print("co", course)


        # try:
        if Grade.objects.filter(course= course, student = student).exists():
            

            return Response({"Failure": "This is a duplicate. The Student already has the grade for the Course"}, status=status.HTTP_400_BAD_REQUEST)

        grade_serializer = GradeSerializer(data=grade_data)
        # print("grade_serializer",grade_serializer)
        if grade_serializer.is_valid():
            grade_serializer.save()
            return JsonResponse(grade_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(grade_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Grade.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} students were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'PUT', 'DELETE'])
def grade_detail(request, pk):
    try:
        grade = Grade.objects.get(pk=pk)
        # print("grade", grade)
        # grade = Grade.objects.filter(student=pk)
    except Grade.DoesNotExist:
        return JsonResponse({'message': 'The student does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        grade_serializer = GradeSerializer(grade)
        return JsonResponse(grade_serializer.data)

    elif request.method == 'PUT':
        grade_data = JSONParser().parse(request)
        grade_serializer = GradeSerializer(grade, data=grade_data)
        if grade_serializer.is_valid():
            grade_serializer.save()
            return JsonResponse(grade_serializer.data)
        return JsonResponse(grade_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        grade.delete()
        return JsonResponse({'message': 'Grade was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)





#------------------------------------------------ Attendance ------------------------------------------------------

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def attendance_list(request):
    if request.method == 'GET':
        attends = Attendance.objects.all()

        attend = request.GET.get('student', None)
        if attend is not None:
            attends = attends.filter(student__icontains=attend)

        attends_serializer = AttendanceSerializer(attends, many=True)
        return JsonResponse(attends_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        attend_data = JSONParser().parse(request)
        # print("grade_data",grade_data)
        # student = Student.objects.all()
        su = attend_data["student"]
        student = Student.objects.get(pk=su)
        # print("s1", student)
        da = attend_data["course"]
        course = Course.objects.get(pk=da)
        # print("co", course)
        at = attend_data["date_of_attendance"]
        # atten_date = Grade

        # try:
        if Attendance.objects.filter(course= course, student = student, date_of_attendance = at).exists():
            

            return Response({"Failure": "This is a duplicate. The Student already has the attendance for the Course"}, status=status.HTTP_400_BAD_REQUEST)

        attend_serializer = AttendanceSerializer(data=attend_data)
        # print("grade_serializer",grade_serializer)
        if attend_serializer.is_valid():
            attend_serializer.save()
            return JsonResponse(attend_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(attend_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Attendance.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} attendances were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'PUT', 'DELETE'])
def attend_detail(request, pk):
    try:
        attend = Attendance.objects.get(pk=pk)
        # print("grade", grade)
        # grade = Grade.objects.filter(student=pk)
    except Attendance.DoesNotExist:
        return JsonResponse({'message': 'The attendance does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        attend_serializer = AttendanceSerializer(attend)
        return JsonResponse(attend_serializer.data)

    elif request.method == 'PUT':
        attend_data = JSONParser().parse(request)
        attend_serializer = AttendanceSerializer(attend, data=attend_data)
        if attend_serializer.is_valid():
            attend_serializer.save()
            return JsonResponse(attend_serializer.data)
        return JsonResponse(attend_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        attend.delete()
        return JsonResponse({'message': 'Attendance was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
