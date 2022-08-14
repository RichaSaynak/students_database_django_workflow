from django.urls import path
from instructors import views as instructors_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', instructors_views.index, name='index'),
    path('', instructors_views.index1.as_view(), name='home_instructor'),
    path('api/instructors/', instructors_views.instructor_list),
    path('api/instructors/<int:pk>/', instructors_views.instructor_detail),
    path('api/instructors/course/<int:course_id>/', instructors_views.instructor_list_course)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
