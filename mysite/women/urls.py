

from django.urls import path
from . import views

urlpatterns = [
    path('women/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('category/<int:category_id>/', views.show_category, name='category'),
]
