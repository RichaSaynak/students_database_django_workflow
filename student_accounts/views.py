from django.shortcuts import render

from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from student_accounts.models import Student_Account
from student_accounts.serializers import Student_AccountSerializer, Student_AccountSerializer2
from django.http import HttpResponse

import hashlib
import secrets



def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()




# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the student_account_accounts index.")




def index1(request):
    print("------------------------- I AM HERE")
    queryset = Student_Account.objects.all()
    return render(request, "student_accounts/index.html", {'student_accounts': queryset})


class index1(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_accounts/index.html'

    def get(self, request):
        queryset = Student_Account.objects.all()
        return Response({'student_accounts': queryset})




class list_all_student_accounts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_accounts/student_account_list.html'

    def get(self, request):
        queryset = Student_Account.objects.all()
        return Response({'student_accounts': queryset})




# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def student_account_list(request):
    if request.method == 'GET':
        student_accounts = Student_Account.objects.all()


        name = request.GET.get('username', None)
        if name is not None:
            student_accounts = student_accounts.filter(username__icontains=name)

        student_accounts_serializer = Student_AccountSerializer2(student_accounts, many=True)
        return JsonResponse(student_accounts_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        student_account_data = JSONParser().parse(request)
        # print(student_account_data)
        student_account_data["password"] = scramble(student_account_data["password"])
        student_account_serializer = Student_AccountSerializer(data=student_account_data)
        if student_account_serializer.is_valid():
            student_account_serializer.save()
            # print("serial",student_account_serializer.data )
            # student_account_data = student_account_data.pop("password")
            # student_account_serializer = Student_AccountSerializer2(data=student_account_data)
            # if student_account_serializer.is_valid():
                # print(student_account_serializer.data)
            return JsonResponse(student_account_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(student_account_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Student_Account.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} student_accounts were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def student_account_detail(request, pk):
    try:
        student_account = Student_Account.objects.get(pk=pk)
        
    except Student_Account.DoesNotExist:
        return JsonResponse({'message': 'The student_account does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # student_account = Student_Account.objects.values_list('id','username')
        student_account_serializer = Student_AccountSerializer2(student_account)
        return JsonResponse(student_account_serializer.data)

    elif request.method == 'PUT':
        student_account_data = JSONParser().parse(request)
        student_account_data["password"] = scramble(student_account_data["password"])
        student_account_serializer = Student_AccountSerializer(student_account, data=student_account_data)
        if student_account_serializer.is_valid():
            student_account_serializer.save()
            return JsonResponse(student_account_serializer.data)
        return JsonResponse(student_account_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student_account.delete()
        return JsonResponse({'message': 'student_account was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def student_account_list_published(request):
#     student_accounts = Student_Account.objects.filter(published=True)

#     if request.method == 'GET':
#         student_accounts_serializer = Student_AccountSerializer(student_accounts, many=True)
#         return JsonResponse(student_accounts_serializer.data, safe=False)

