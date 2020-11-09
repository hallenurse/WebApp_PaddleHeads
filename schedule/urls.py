from django.urls import path
from .views import (
    ScheduleListView,
    ScheduleUpdateView,
    ScheduleDetailView,
    ScheduleDeleteView,
    ScheduleCreateView,
    )

urlpatterns = [   
    path('<int:pk>/edit/', ScheduleUpdateView.as_view(), name='schedule_edit'),
    path('', ScheduleListView.as_view(), name='schedule_list'),
    path('<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),
    path('new/', ScheduleCreateView.as_view(), name = 'schedule_new'),
    path('', ScheduleListView.as_view(), name='schedule_list')
    ]
