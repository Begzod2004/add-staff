from unicodedata import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.db.models import *
from django.contrib.auth import *
from django.contrib.auth import login


class StaffListView(ListView):
    template_name = 'Staff.html'
    context_object_name = "Staff"
    model = Staff


class StaffDetailView(DetailView):
    template_name = 'staff-detail.html'
    model = Staff 




class StaffCreateView(CreateView):
    queryset = Staff.objects.all()
    template_name = 'Staff-add.html'
    fields = "__all__"

    success_url = '/Staff'


class StaffUpdateView(UpdateView):
    queryset = Staff.objects.all()
    template_name = 'Staff-add.html'
    fields = "__all__"
    context_object_name = 'Staff'
    success_url = '/Staff'


class StaffDeleteView(DeleteView):
    queryset = Staff.objects.all()
    template_name = 'Staff-delete.html'
    fields = "__all__"

    success_url = '/Staff'



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['staff'] = staff.objects.filter(
    #         region=self.kwargs['pk'])
    #     return context




class GenderListView(ListView):
    template_name = 'gender.html'
    context_object_name = "Gender"
    model = Gender


class GenderCreateView(CreateView):
    queryset = Gender.objects.all()
    template_name = 'Gender-add.html'
    fields = "__all__"
    success_url = '/Gender'


class GenderUpdateView(UpdateView):
    queryset = Gender.objects.all()
    template_name = 'Gender-add.html'
    fields = "__all__"
    context_object_name = 'Gender'
    success_url = '/Gender'
    

class GenderDeleteView(DeleteView):
    queryset = Gender.objects.all()
    template_name = 'Gender-delete.html'
    fields = "__all__"
    success_url = '/Gender'


