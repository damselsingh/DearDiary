from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('update/<int:pk>/', views.update_diary, name="update_diary"),
    path('delete_diary/<int:pk>/', views.delete_diary, name="delete_diary"),
    path('see-all/', views.see, name='see')
]
