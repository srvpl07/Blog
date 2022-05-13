from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('posts/', views.PostView.as_view({'get':'list','post':'create'}), name='post'),
    path('posts/<int:pk>', views.PostView.as_view({'delete':'destroy','put':'update'}), name='post_1'),

]
