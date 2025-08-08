from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clock/', views.clock, name='clock'),
    path('about/<int:person_id>/', views.about, name='about'),
    path('persons/', views.persons, name='persons'),
    path('timeinout/', views.persons, name='persons'),
    path('sheet/<int:year>/<int:month>/<int:day>', views.sheet, name='sheet'),
]
