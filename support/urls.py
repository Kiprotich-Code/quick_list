from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('support/message/', views.create_message, name='create_message'),
    path('support/waitlist/', views.add_waitlist, name='add_waitlist'),
]