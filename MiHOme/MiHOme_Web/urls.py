from django.urls import path, register_converter
from . import views, converter

register_converter(converter.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('post_db/<slug:cat_slug>/', views.post_db, name='post_db'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('room/<int:room_id>', views.room, name='room'),
    path('archive/<yyyy:year>/', views.archive, name='archive'),
]
