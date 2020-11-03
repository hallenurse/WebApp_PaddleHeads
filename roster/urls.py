from django.urls import path
from .views import (
    RosterListView,
    RosterUpdateView,
    RosterDetailView,
    RosterDeleteView,
    RosterCreateView,
    )
urlpatterns = [
    path('<int:pk>/edit/', RosterUpdateView.as_view(), name='roster_edit'),
    path('<int:pk>/', RosterDetailView.as_view(), name='roster_detail'),
    path('<int:pk>/delete/', RosterDeleteView.as_view(), name='roster_delete'),
    path('new/', RosterCreateView.as_view(), name = 'roster_new'),
    path('',RosterListView.as_view(), name='roster_list')
    ]
