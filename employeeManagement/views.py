from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

from .models import Employee
from .forms import EmployeeForm

def EmployeeManagementPage(request):
    employees_list = Employee.objects.order_by('id')

    form = EmployeeForm()

    context = {'employees_list': employees_list, 'form': form}
    return render(request, 'employeeManagement/index.html', context=context)

@require_POST
def AddEmployee(request):
    form = EmployeeForm(request.POST)
    print(request.POST['name'])
    if form.is_valid():
        new_employee = Employee(name=request.POST['name'], email=request.POST['email'], department=request.POST['department'])
        new_employee.save()
    return redirect('/employeeManagement')

def DeleteEmployee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.delete()
    return redirect('/employeeManagement')
