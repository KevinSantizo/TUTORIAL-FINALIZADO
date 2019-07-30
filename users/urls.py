from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('new/', views.register_user, name='new'),
]