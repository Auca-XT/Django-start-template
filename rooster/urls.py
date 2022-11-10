from django.urls import path

from .views import (
DienstCreateView, DienstDetailView, DienstListView, DienstUpdateView
)

app_name = 'rooster'
urlpatterns = [
path('dienst/<int:pk>/update/', DienstUpdateView.as_view(), name='update'),
path('dienst/create/', DienstCreateView.as_view(), name='create'),  
path('dienst/<int:pk>/', DienstDetailView.as_view(), name='detail'),  
path('', DienstListView.as_view(), name='list'),
]