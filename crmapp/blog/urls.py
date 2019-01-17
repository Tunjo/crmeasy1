from django.conf.urls import url
from .views import BlogList
from .views import BlogDelete



urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^new/$', 'crmapp.blog.views.blog_new', name='blog_new'),
    url(r'^(?P<id>[\d\w-]+)/edit/$', 'crmapp.blog.views.blog_update', name='blog_update'),
    url(r'^(?P<id>[\d\w-]+)/user/$', 'crmapp.blog.views.user_list_blog', name='user_list_blog'),
    url(r'^(?P<pk>[\d\w-]+)/delete/$', BlogDelete.as_view(), name='blog_delete')

]