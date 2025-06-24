from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('course/', views.course, name='course'),
    path('add_course/', views.add_course, name='add_course'),
    path('update_course/<str:course_id>/', views.update_course, name='update_course'),
    path('delete_course/<str:course_id>/', views.delete_course, name='delete_course'),
    path('exam/', views.exam, name='exam'),
    path('add_exam/', views.add_exam, name='add_exam'),
    path('update_exam/<str:exam_id>/', views.update_exam, name='update_exam'),
    path('delete_exam/<str:exam_id>/', views.delete_exam, name='delete_exam'),
    path('result/', views.result, name='result'),
    path('add_result/', views.add_result, name='add_result'),
    path('update_result/<int:student_id>/', views.update_result, name='update_result'),
    path('delete_result/<int:student_id>/', views.delete_result, name='delete_result'),
    path('staff/', views.staff, name='staff'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('update_staff/<str:staff_id>/', views.update_staff, name='update_staff'),
    path('delete_staff/<str:staff_id>/', views.delete_staff, name='delete_staff'),
]