from django.urls import path

from . import views

app_name = 'bboard'

urlpatterns = [
    path('add/', views.BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('', views.index, name='index'),
]