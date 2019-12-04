from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('project_justification/', project_justification_list, name='project_justification_list_url'),
    path('project_justification/create', ProjectJustificationCreate.as_view(), name='project_justification_create_url'),
    path('project_justification/detail/<int:id>/', ProjectDetail.as_view(), name='project_justification_detail_url')
]
