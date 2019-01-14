from django.conf.urls import url


urlpatterns = [

    url(r'^new/$', 'crmapp.contacts.views.contact_cru', name='contact_new'),



    url(r'^(?P<uuid>[\d\w-]+)/$',
        'crmapp.contacts.views.contact_detail', name="contact_detail"),

    url(r'^(?P<uuid>[\d\w-]+)/edit/$', 'crmapp.contacts.views.contact_cru', name='contact_update'),




]