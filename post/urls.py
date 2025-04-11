from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.post_detail_view, name='post_detail'),
]
