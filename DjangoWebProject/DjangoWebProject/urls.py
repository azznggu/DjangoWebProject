"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include, url
import HelloDjangoApp.views

urlpatterns = [
        url(r'^$', HelloDjangoApp.views.index, name = 'index'),
        url(r'^home$', HelloDjangoApp.views.home, name = 'home'),
        url(r'^about$', HelloDjangoApp.views.about, name = 'about'),
]



# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = [
#    # Examples:
#    url(r'^$', app.views.home, name='home'),
#    url(r'^contact$', app.views.contact, name='contact'),
#    url(r'^about', app.views.about, name='about'),
#    url(r'^login/$',
#        django.contrib.auth.views.login,
#        {
#            'template_name': 'app/login.html',
#            'authentication_form': app.forms.BootstrapAuthenticationForm,
#            'extra_context':
#            {
#                'title': 'Log in',
#                'year': datetime.now().year,
#            }
#        },
#        name='login'),
#    url(r'^logout$',
#        django.contrib.auth.views.logout,
#        {
#            'next_page': '/',
#        },
#        name='logout'),

#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#]
