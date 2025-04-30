from django.contrib import admin
from django.urls import path
from todolist import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo'), # To do List 확인
    path('todo/<int:pk>/', views.todo_info, name='info'), # To do의 상세 정보를 볼 수 있는 페이지
    path('admin/', admin.site.urls),
]
