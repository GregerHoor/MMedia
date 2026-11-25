from django.urls import path
from . import views
from .views import CUD_Functions as cud

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('courses/', views.courses, name='courses'),
    path('courses_select/<uuid:token>/', views.courses_select, name='course_select'),

    path('add_content/', views.add, name='add_content'),
    path('delete_content/<uuid:token>/', views.delete, name='delete_content'),
    path('edit_content/<uuid:token>/', views.edit, name='edit_content'),
    
    path('staff/', views.login_staff, name='staff'),
    path('logout/', views.logout, name='logout'),
    path('reg_staff/', views.register_staff, name='reg_staff'),
    path('community/', views.community, name='community'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('help_center/', views.help_center, name='help_center'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_n_condition/', views.terms_n_condition, name='terms_n_condition'),
]