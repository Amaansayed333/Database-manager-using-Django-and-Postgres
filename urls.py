from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.display, name='display'),
    path('getting/', views.getting, name='getting'),
    path('showlist/', views.showlist, name='showlist'),
    path('update/<int:id>/', views.update_entry, name='update_entry'),
    path('delete/<int:id>/', views.delete_entry, name='delete_entry'),
]
