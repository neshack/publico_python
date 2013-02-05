from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'admhosting.views.home', name='home'),
    # url(r'^admhosting/', include('admhosting.foo.urls')),
    url(r'^$','principal.views.lista_clientes'),
    url(r'^cuentas','principal.views.lista_cuentas'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
)
