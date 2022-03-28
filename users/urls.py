from django.urls import path, include
# 从自己当前文件目录导入
from . import views

app_name = 'users'
urlpatterns = [
    # 包含默认的身份验证url
    path('', include('django.contrib.auth.urls')),
    # 注册页面
    path('register/', views.register, name='register'),
]
