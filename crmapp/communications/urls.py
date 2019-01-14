from django.conf.urls import url
from .views import CommDelete


urlpatterns = [
    url(r'^/new/$', 'crmapp.communications.views.comm_cru', name='comm_new'),
    url(r'^(?P<uuid>[\d\w-]+)/edit/$', 'crmapp.communications.views.comm_cru', name='comm_update'),
    url(r'^(?P<pk>[\d\w-]+)/delete/$', CommDelete.as_view(), name='comm_delete'),

    url(r'^(?P<uuid>[\d\w-]+)/$', 'crmapp.communications.views.comm_detail', name='comm_detail'),


]
