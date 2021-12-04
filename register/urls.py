from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'),
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('list/', views.employee_list, name='employee_list'),
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
]
