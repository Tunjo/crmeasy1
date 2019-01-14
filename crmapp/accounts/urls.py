from django.conf.urls import url
from .views import AccountList


urlpatterns = [
    url(r'^list/$', AccountList.as_view(), name='account_list'),



    url(r'^new/$',
        'crmapp.accounts.views.account_cru', name='account_new'),


    # regular expretions uuid
    url(r'^(?P<uuid>[\d\w-]+)/$',
        'crmapp.accounts.views.account_detail', name='account_detail'),

    url(r'^(?P<uuid>[\d\w-]+)/edit/$',
        'crmapp.accounts.views.account_cru', name='account_update'),

]
