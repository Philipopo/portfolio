from django import views
from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.dashboard, name="dashboard"),    
    path('add-project', views.add_project, name="add_project"),
    path('add-category', views.add_category, name="add_category"),
    path('category/<str:cats>/', views.category_view, name='category'),
    path('files/', views.UploadView, name='upload'),
    
]

