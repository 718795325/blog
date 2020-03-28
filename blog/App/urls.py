"""Django_Projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from App import views
app_name='App'
urlpatterns = [

    #首页
    path('index/',views.index,name='index'),
    #导航栏
    path('header/',views.header,name='header'),
    #登录
    path('loginb/',views.loginb,name='loginb'),
    #logout
    path('logout/',views.logout,name='logout'),
    #左边导航栏
    path('left/',views.left,name='left'),
    #新闻
    path('xinwen/',views.xinwen,name='xinwen'),
    path('xinwen/<int:cid>/',views.xinwen,name='xinwen'),
    path('xinwen/<int:cid>/<int:page>/',views.xinwen,name='xinwen'),
    #文章内容
    path('content/<int:aid>/',views.content,name='content'),
    #修改密码
    path('changepaswd/',views.changepaswd,name='changpaswd'),
    #注册
    path('register/',views.register,name='register'),
    #删除文章
    path('art_del/<int:aid>/<int:cid>/<int:page>/',views.art_del,name='art_del'),
    #文章修改
    path('art_pub/<int:aid>/',views.art_pub,name='art_pub'),
    #文章发布
    path('art_publick/<int:cid>/',views.art_publick,name='art_publick'),
    #增加栏目
    path('add_car/<name>/',views.add_car,name='add_car'),
    #删除栏目
    path('del_car/<name>',views.del_car,name='del_car'),
    #短信验证
    # path('send_em/',views.send_em,name='send_em'),
    # path('text1/',views.text1,name='text1'),
    # 富文本框
    path('wenbenbianji/',views.wenbenbianji,name='wenbenbianji'),
    #插入数据
    path('charu/',views.charu,name='charu/'),
    #验证码
    # path('cap/',views.cap,name='cap'),


]
