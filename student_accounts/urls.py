from django.urls import path
from student_accounts import views as student_accounts_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', student_accounts_views.index, name='home'),
    path('', student_accounts_views.index1.as_view(), name='home_account'),
    path('api/student_accounts/', student_accounts_views.student_account_list),
    path('api/student_accounts/<int:pk>/', student_accounts_views.student_account_detail),
    # path('api/student_accounts/published/', student_accounts_views.student_account_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)