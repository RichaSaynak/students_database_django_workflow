from django.urls import path
from students import views as students_views
from django.conf.urls.static import static
from django.conf import settings

# from . import views

urlpatterns = [
    # path('', students_views.index, name='index'),
    path('', students_views.index1.as_view(), name='home_student'),
    path('api/students/', students_views.student_list),
    path('api/students/<int:pk>/', students_views.student_detail),
    path('api/students/address/<str:address>/', students_views.student_list_address),
    path('api/grades/', students_views.grade_list),
    path('api/grades/<int:pk>/', students_views.grade_detail),
    path('api/attendances/', students_views.attendance_list),
    path('api/attendances/<int:pk>/', students_views.attend_detail),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

