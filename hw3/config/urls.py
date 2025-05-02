from django.contrib import admin
from django.urls import path, include

from todo.views import todo_list, todo_info
from users.views import signup, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list, name='todo_list'),
    path('<int:pk>/', todo_info, name='todo_info'),
    # 로그아웃
    path('accounts/', include('django.contrib.auth.urls')),
    # 회원가입
    path('signup/', signup, name='signup'),
    # 로그인
    path('login/', login, name='login'),
]
