from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokedex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'pokemon.views.index'),
    url(r'^pokemon/(?P<id>\d)/$', 'pokemon.views.pokemon'),
    url(r'^admin/', include(admin.site.urls)),
)
