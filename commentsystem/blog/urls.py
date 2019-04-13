from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('detail/addComment/<int:post_id>', views.add_comment_to_post, name='addcomment'),
    path('detail/addReComment/<int:comment_id>', views.add_recomment_to_comment, name='addrecomment'),
    path('detail/getComment/<int:post_id>', views.get_comments_to_post, name='getcomment'),
]