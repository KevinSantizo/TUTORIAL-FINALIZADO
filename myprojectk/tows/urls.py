from django.urls import path
from tows import views


app_name = 'tows'
urlpatterns = [
    path('page/', views.show_assignment, name='page')
]