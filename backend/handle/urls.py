from django.urls import path
from . import views


urlpatterns = [
    path('init', views.handle_init),
    path('pre', views.handle_pre),
    path('select', views.handle_select),
    path('select-picture', views.handle_select_picture)
]
