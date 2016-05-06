"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns: S url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from practice.views import todolist, todoitem, todoitemnew, todoitemComplete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todolist/$', todolist,name="todolist"),
    url(r'^todoitem/(?P<list_id>\d+)/$', todoitem,name="todoitem"),
    url(r'^todoitem/(?P<item_id>\d+)/editname/$', todoitemnew,name="todoitemnew"),
    url(r'^todoitem/(?P<item_id>\d+)/complete/$', todoitemComplete,name="todoitemComplete"),
    #url(r'^todoitem/(?P<item_id>\d+)/complete/$', todoGet,name="todoGet),
    
    ]
