from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

from marketing.views import HomePage

urlpatterns = [



    # Marketing pages

    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs

    url(r'^signup/$', 'crmapp.subscribers.views.subscribe_new', name='sub_new'),

    # Login/log out

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
    #ACC URLS:
    url(r'^account/', include('crmapp.accounts.urls')),

    url(r'^contact/', include('crmapp.contacts.urls')),

    url(r'^comm/', include('crmapp.communications.urls')),

    url(r'^admin/', include(admin.site.urls)),

]
