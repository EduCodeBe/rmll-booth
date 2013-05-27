from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from askforabooth.models import boothDemand
import settings
from django.utils.functional import lazy
reverse_lazy = lambda name=None, *args : lazy(reverse, str)(name, args=args)
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'booths.views.home', name='home'),
    url(r'^success$', TemplateView.as_view(template_name="askforabooth/success.html"), name='success'),
    url(r'^$', CreateView.as_view(model=boothDemand, success_url=reverse_lazy('success'))),
    url(r'^admin/', include(admin.site.urls)),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
