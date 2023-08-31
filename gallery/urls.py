from django.urls import path
from . import views

urlpatterns = [
    path('', views.Base, name='base'),
    path('portfolio', views.Portfolio, name='portfolio'),
    path('about', views.About, name='about'),
    path('testimonials', views.Testimonials, name='testimonials'),
    path('services', views.Service, name='services'),


    path('contact', views.Contact, name='contact'),
    path('categories/<str:category_name>/', views.Catagories, name='categories'),  # Corrected view name
    path('categories/kids/', views.Kids, name='kids'),
    path('categories/couples/', views.Couples, name='couples'),
    path('category/<int:category_id>/', views.CategoryPhotos, name='category_photo'),
    path('upload', views.Upload, name='upload'),
    # Add more URL patterns as needed
]
