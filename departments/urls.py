from django.urls import path
from . import views

urlpatterns = [
    path('', views.DepartmentTemplateView.as_view(), name='department_tree'),
]