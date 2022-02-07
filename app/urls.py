from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path(r'', views.index, name='index'),
    path("ajax/", views.call_paraphrase, name="call_paraphrase"),
    path("ajax/", views.call_convert, name="call_convert"),
    path("ajax/", views.call_write_data, name="call_write_data"),
]