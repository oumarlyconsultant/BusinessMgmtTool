from django.urls import path
from . import views

app_name = 'employeeMgmt'

urlpatterns = [
# post views
path('', views.employee_list, name='employee_list'),
path('<int:id>/', views.employee_detail, name='employee_detail'),
]