from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    MyPostedListView,
    MyFriendsListView,
    MyDashboardView
    # UsersView,
    # DraftPostListView,
    # ArchivedPostListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('posted/', MyPostedListView.as_view(), name='my_posted_list'),
    path('posted/', MyPostedListView.as_view(), name='my_posted_list'),

    path('friends/', MyFriendsListView.as_view(), name='my_friends_list'),
    path('dashboard/', MyDashboardView.as_view(), name='my_dashboard'),
    
]