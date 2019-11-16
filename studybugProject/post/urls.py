from django.urls import path
from .import views

urlpatterns = [
    #포스트 페이지
    path('',views.Post,name='list'),
    # path('<category_id>',views.Mpost,name='mlist'),
    path('new/',views.PostNew,name='new'),
    path('show/<int:post_id>',views.PostShow,name='detail'),
    path('edit/<int:post_id>',views.PostEdit,name='change'),
    #path('update/<int:post_id>',views.PostUpdate,name='update'),
    path('delete/<int:post_id>',views.PostDelete,name='delete'),
    path('show/commentcreate/<int:post_id>',views.commentcreate,name='commentcreate'),
    path('show/commentdelete/<int:post_id>/<int:comment_id>',views.commentdelete,name='commentdelete'),
]