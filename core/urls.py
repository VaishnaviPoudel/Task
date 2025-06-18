from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('add_water_intake/', views.add_water_intake, name='add_water_intake'),
    path('history/', views.weekly_history, name='weekly_history'),
    path('set_goal/', views.update_goal, name='set_goal'),

    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),


]