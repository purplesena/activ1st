from django.urls import path
from .views import ProtestListView, PostEditView, PostListView, PostDetailView, PostDeleteView, CommentDeleteView, ProfileEditView, ProfileView, AddFollower, RemoveFollower, ProtestDetailView, AddLike, AddDislike, Search,  ListFollowers, ProtestDeleteView

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
    path('protests', ProtestListView.as_view(), name='protests'),
    path('protests/<int:pk>', ProtestDetailView.as_view(), name='protest-detail'),
    path('protest/delete/<int:pk>', ProtestDeleteView.as_view(), name='protest-delete'),
    path('search/', Search.as_view(), name='search'),
    path('profile/<int:pk>/followers', ListFollowers.as_view(), name='followers-list'),
]

#comment/delete/<int:pk>