from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from .models import Service
from .models import Appointment

from .forms import ServiceForm
from .forms import AppointmentForm


class HomeView(TemplateView):

    template_name = 'home.html'


class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['total_services'] = Service.objects.count()

        context['total_appointments'] = Appointment.objects.count()

        context['pending'] = Appointment.objects.filter(
            status='pending'
        ).count()

        context['completed'] = Appointment.objects.filter(
            status='completed'
        ).count()

        context['attending'] = Appointment.objects.filter(
            status='attending'
        ).count()

        return context


class ServiceListView(ListView):

    model = Service

    template_name = 'services/service_list.html'


class ServiceCreateView(LoginRequiredMixin, CreateView):

    model = Service

    form_class = ServiceForm

    template_name = 'services/service_form.html'

    success_url = reverse_lazy('service_list')


class ServiceUpdateView(LoginRequiredMixin, UpdateView):

    model = Service

    form_class = ServiceForm

    template_name = 'services/service_form.html'

    success_url = reverse_lazy('service_list')


class ServiceDeleteView(LoginRequiredMixin, DeleteView):

    model = Service

    template_name = 'services/service_confirm_delete.html'

    success_url = reverse_lazy('service_list')


class AppointmentListView(ListView):

    model = Appointment

    template_name = 'appointments/appointment_list.html'


class AppointmentCreateView(CreateView):

    model = Appointment

    form_class = AppointmentForm

    template_name = 'appointments/appointment_form.html'

    success_url = reverse_lazy('appointment_list')

    def form_valid(self, form):

        messages.success(
            self.request,
            'Turno reservado correctamente'
        )

        return super().form_valid(form)


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):

    model = Appointment

    fields = ['status']

    template_name = 'appointments/appointment_update.html'

    success_url = reverse_lazy('appointment_list')