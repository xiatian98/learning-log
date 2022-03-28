"""定义learning_logs的URL模式 路由"""

from django.urls import path, re_path
# .从当前文件夹导入
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有的主题
    path('topics/', views.topics, name='topics'),
    # 特定主题的页面 有名分组 别名topic 前端中可以使用{% url '别名' %}来访问页面
    re_path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    # 用于添加新主题的页面
    path('new_topic/', views.new_topic, name='new_topic'),
    # 用于添加新条目的页面 无名分组
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 编辑条目
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]

