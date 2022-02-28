from django.urls import path
from . import views
from .views import detail_view


app_name = 'firstApp'
urlpatterns = [
  path('', views.index, name='index'),
  path('new', views.new_question, name='new_question'),
  path('questions', views.questions_lit, name='questions_lit'),
  path('<id>', detail_view ),
]