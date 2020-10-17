"""django_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('create/', views.CreateBlog_page.as_view(), name="create_blog_page"),
    path('<int:pk>/', views.DetailBlog_page.as_view(), name="detail_blog_page"),
    path('<int:pk>/update/', views.UpdateBlog_page.as_view(), name="update_blog_page"),
    path('<int:pk>/delete/', views.DeleteBlog_page.as_view(), name="delete_blog_page"),
]
