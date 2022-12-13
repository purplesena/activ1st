from django.urls import path
from .views import EventListView, PostEditView, PostListView, PostDetailView, PostDeleteView, CommentDeleteView, ProfileEditView, ProfileView, AddFollower, RemoveFollower, EventDetailView, EventEditView, EventDeleteView, AddLike, AddDislike, UserSearch

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('events', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('events/edit/<int:pk>', EventEditView.as_view(), name='event-edit'),
    path('events/delete/<int:pk>', EventDeleteView.as_view(), name='event-delete'),
    path('search/', UserSearch.as_view(), name='profile-search')
]

#comment/delete/<int:pk>