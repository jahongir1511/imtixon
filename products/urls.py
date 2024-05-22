from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('dori-list/', DoriListView.as_view(), name='dori-list'),
    path('detail/<int:pk>/', DoriDetailView.as_view(), name='dori-detail'),
    path('delete/<int:pk>/', DoriDeleteView.as_view(), name='dori-delete'),
    path('create/', DoriCreateView.as_view(), name='create-dori'),
    path('add_review/<int:pk>/', AddReviewView.as_view(), name='add-review'),
    path('edit_review/<int:pk>/', ReviewUpdateView.as_view(), name='edit-review'),
    path('category/', CategoriesListView.as_view(), name='category'),
]
