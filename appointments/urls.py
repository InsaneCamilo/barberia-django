from django.urls import path

from .views import *

urlpatterns = [

    path('', HomeView.as_view(), name='home'),

    path('services/', ServiceListView.as_view(), name='service_list'),

    path('services/create/', ServiceCreateView.as_view(), name='service_create'),

    path(
        'services/<int:pk>/update/',
        ServiceUpdateView.as_view(),
        name='service_update'
    ),

    path(
        'services/<int:pk>/delete/',
        ServiceDeleteView.as_view(),
        name='service_delete'
    ),

    path(
        'appointments/',
        AppointmentListView.as_view(),
        name='appointment_list'
    ),

    path(
        'appointments/create/',
        AppointmentCreateView.as_view(),
        name='appointment_create'
    ),

    path(
        'appointments/<int:pk>/update/',
        AppointmentUpdateView.as_view(),
        name='appointment_update'
    ),
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard'
    ),
]