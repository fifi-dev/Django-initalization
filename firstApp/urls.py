from django.urls import path
from . import views
# importing views from views..py
from .views import detail_view
from .views import update_view
from .views import delete_view


app_name = 'firstApp'
urlpatterns = [
  path('', views.index, name='index'),
  path('new', views.new_question, name='new_question'),
  path('questions', views.questions_lit, name='questions_lit'),
  path('<id>', detail_view ),
  path('<id>/update', update_view ),
  path('<id>/delete', delete_view ),
]