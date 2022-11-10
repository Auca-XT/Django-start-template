from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Dienst

class DienstCreateView(CreateView):
    model = Dienst
    fields = ['question', 'answer']

class DienstDetailView(DetailView):
    model = Dienst
  
class DienstListView(ListView):
    model = Dienst

class DienstUpdateView(UpdateView):
    model = Dienst
    fields = ['question', 'answer']
# Create your views here.
