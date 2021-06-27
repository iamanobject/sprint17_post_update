from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.author_list, name='authors'),
    path('list/', views.author_list, name='authors_list'),
    path('<int:pk>/delete', views.AuthorDeleteView.as_view(), name='author_delete'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update', views.AuthorUpdateView.as_view(), name='author_update')
]