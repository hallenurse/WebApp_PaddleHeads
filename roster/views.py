from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Roster

class RosterListView(ListView):
    model = Roster
    template_name = 'roster_list.html'

class RosterDetailView(DetailView):
    model = Roster
    template_name = 'roster_detail.html'

class RosterUpdateView(UpdateView):
    model = Roster
    fields = ('profile', 'batting_average',)
    template_name = 'roster_edit.html'

class RosterDeleteView(DeleteView):
    model = Roster
    template_name = 'roster_delete.html'
    success_url = reverse_lazy('roster_list')

class RosterCreateView(CreateView):
    model = Roster
    template_name = 'roster_new.html'
    fields = ('name', 'number', 'profile', 'batting_average', 'author',)
