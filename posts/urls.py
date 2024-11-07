from django.urls import path
from .views import indexView, detailView, savePostView, thanksView, updateView, deleteView, guestView, tagDetails, search
from . import views

urlpatterns = [
    path('home/', views.IndexViewListClass.as_view(), name="posts-home"),
    path('guest/', guestView, name="posts-guest"),
    path('details/<int:pk>', views.PostDetailsClass.as_view(), name="post-detail"),
    path('save', savePostView, name="post-create"),
    path('thanks', thanksView, name="post-thanks"),
    path('update/<int:id>', updateView, name="post-update"),
    path('delete/<int:id>', deleteView, name="post-delete"),
    path('tag/details/<int:pk>', views.TagDetailsClass.as_view(), name="tag-detail"),
    path('search', views.SearchViewClass.as_view(), name="posts-search"),
]