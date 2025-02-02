from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # User Authentication URLs
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search_hotels, name='search_results'),

    # Search and Comparison URLs
    path('search/', views.search_hotels, name='search_hotels'),
    path('compare/', views.compare_hotels, name='compare_hotels'),

    # Bookmark URLs
    path('bookmarks/', views.bookmark_list, name='bookmarks'),
    path('bookmark/<int:hotel_id>/', views.bookmark_hotel, name='bookmark_hotel'),
]
