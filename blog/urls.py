from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('blog-details/<slug>/', views.blogDetails, name='blog-details'),
    #     path('post-details/<slug>/', views.post_details,
    #          name='post_details')
]
