from django.urls import *
from .views import *
from django.urls import path



urlpatterns = [
      # Staff
    path('', StaffListView.as_view(), name='Staff'),
    path('Staff', StaffListView.as_view(), name='Staff'),
    path('Staff/add', StaffCreateView.as_view(), name='Staff-add'),
    path('Staff/change/<int:pk>', StaffUpdateView.as_view(), name='Staff-change'),
    path('Staff/<int:pk>', StaffDetailView.as_view(), name='Staff-DetailView'),
    path('Staff/delete/<int:pk>', StaffDeleteView.as_view(), name='Staff-delete') ,
      #  Gender

    path('Gender/', GenderListView.as_view(), name='Gender'),
    path('Gender/add', GenderCreateView.as_view(), name='Gender-add'),
    path('Gender/change/<int:pk>', GenderUpdateView.as_view(), name='Gender-change'),
    path('Gender/delete/<int:pk>', GenderDeleteView.as_view(), name='Gender-delete') ,



    ] 
  

