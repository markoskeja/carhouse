from django.urls import path

from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('article/', views.article, name="article"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('editorpage/', views.editorpage, name="editorpage"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('accessLogin/', views.accessLogin, name="accessLogin"),
    path("logout/", views.logout, name= "logout"),
]