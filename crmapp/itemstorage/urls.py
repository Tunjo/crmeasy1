from django.conf.urls import url
from .views import ItemList, ItemDelete



urlpatterns = [
    url(r'^$', ItemList.as_view(), name='item_list'),

    url(r'^new/$',
        'crmapp.itemstorage.views.item_new', name='item_new'),

    url(r'^(?P<id>[\d\w-]+)/edit/$', 'crmapp.itemstorage.views.item_update', name='item_edit'),

    url(r'^(?P<pk>[\d\w-]+)/delete/$', ItemDelete.as_view(), name='item_delete')

]
