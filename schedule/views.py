from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Schedule

class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule_list.html'

class ScheduleDetailView(DetailView):
    model = Schedule
    template_name = 'schedule_detail.html'

class ScheduleUpdateView(UpdateView):
    model = Schedule
    fields = ('title', 'location', 'opponent', 'promotion', 'date',)
    template_name = 'schedule_edit.html'

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'schedule_delete.html'
    success_url = reverse_lazy('schedule_list')

class ScheduleCreateView(CreateView):
    model = Schedule
    template_name = 'schedule_new.html'
    fields = ('title', 'date', 'location', 'opponent', 'promotion',)
