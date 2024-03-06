from django.urls import path
from .views import HomeView, CategoryViewList, CategoryUpdateView, CategoryDeleteView, CategoryCreateView, PostCreateView, PostUpdateView, PostDeleteView, PostDeleteView, PostDetailView
from . import views
app_name = 'blog'

urlpatterns = [
    path('HomeView/', HomeView, name="home"),
    path('category/', CategoryViewList, name='category'),
    path('category/<int:pk>/update/', CategoryUpdateView, name='category-update'),
    path('category/<int:pk>/delete/', CategoryDeleteView, name='category-delete'),
    path('category/add/', CategoryCreateView, name='category-create'),
    path('post/add/', PostCreateView, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView, name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView, name='post-delete'),
    # new url
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
]
