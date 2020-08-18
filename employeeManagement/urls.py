from django.urls import path
from . import views
urlpatterns = [
    path('employeeManagement/', views.EmployeeManagementPage, name='EmployeeManagement'),
    path('add/', views.AddEmployee, name='add'),
    path('delete/<employee_id>', views.DeleteEmployee, name='delete'),
]
