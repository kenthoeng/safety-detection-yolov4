from . import views
from django.urls import path

urlpatterns = [
    # Alert POST
    path('images/', views.post_alert, name='post_alert'),
]