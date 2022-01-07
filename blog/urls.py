
from django.urls import path, include

from . import views
from .views import Post, Category
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView
from .views import CategoryView, DeletePostView, AddCategoryView, CategoryListView


urlpatterns = [
   path('', HomeView.as_view(), name = "home"),
   path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
   path('add_post/', AddPostView.as_view(), name ='add_post'),
   path('article/edit/<int:pk>', UpdatePostView.as_view(), name ='update_post'),
   path('article/<int:pk>/delete', DeletePostView.as_view(), name ='delete_post'),

   path('add_category/', AddCategoryView.as_view(), name ='add_category'),
   path('category/<str:cats>/', CategoryView, name= 'category'),
   path('category_list/', CategoryListView, name= 'category_list'),
   

]
