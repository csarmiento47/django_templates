from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('languages/', views.language, name='languages'),
    path('article/', views.article, name='article'),
    path('create-article/', views.create_article, name='create-article'),
    path('employee/', views.employee, name='employee'),
    path('create-employee/', views.create_employee, name='create-employee')
]