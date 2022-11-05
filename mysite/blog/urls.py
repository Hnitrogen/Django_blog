from django.urls import path
from . import views 


urlpatterns = [
        path('', views.post_list,name='post_list') ,
        #  在浏览器域名的地址  , 页面 , 页面的名字
        #  无用= =        ,    调用视图文件夹里面的post_list函数  , 标志视图的url名称
        path('post/<int:pk>/',views.post_detail,name='post_detail') ,
        #       http://127.0.0.1:8000/post/5/
]
