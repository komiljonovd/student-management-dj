from django.urls import path
from .views import login_views,student_views


urlpatterns = [
    path('api/v1/students/', student_views.StudentListCreateApi.as_view(), name='student-create-list'),
    path('api/v1/students/<int:pk>/', student_views.StudentDetailApi.as_view(), name='student-detail'),
    path('api/v1/students/patch/<int:pk>/',student_views.StudentPatchApi.as_view(),name='student-patch'),
    # TOKEN
    path('api/token/login/', login_views.LoginApiView.as_view(), name='custom_login'),
    path('api/token/refresh/', login_views.TokenRefreshApiView.as_view(), name='token_refresh'),


]