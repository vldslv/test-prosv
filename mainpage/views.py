from django.shortcuts import render

from .models import Employee, Departament

# Create your views here.
def index (request):
    try:
        employee_table = Employee.objects.order_by(request.GET['sort_by'])
    except BaseException:
        employee_table = Employee.objects.order_by('id')
    context = {
        'employee_table': employee_table,
    }
    return render(request, 'mainpage/index.html', context)
