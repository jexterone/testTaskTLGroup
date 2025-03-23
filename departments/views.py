from django.shortcuts import render
from django.views.generic import TemplateView

from departments.models import Department


# Create your views here.

class DepartmentTemplateView(TemplateView):
    template_name = 'department.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = Department.objects.filter(parent=None).first()
        context['department'] = department
        return context