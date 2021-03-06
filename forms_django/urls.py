from django.conf.urls import patterns, include, url
from django.contrib import admin

import forms_builder.forms.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'forms_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('dynamic_form.urls', namespace="dynamic_form")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forms/', include(forms_builder.forms.urls)),
)
