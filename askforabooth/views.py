from django.views.generic import CreateView
from askforabooth.models import boothDemand
from booths import settings
from django.utils import translation



class BoothDemandCreateView(CreateView):
    model = boothDemand

    def get_success_url(self):
        return settings.SUCCESS_URL[self.request.LANGUAGE_CODE]

class BoothDemandCreateViewFr(BoothDemandCreateView):

    def get(self, request, *args, **kwargs):
        translation.activate('fr')
        request.LANGUAGE_CODE = 'fr'
        return super(BoothDemandCreateViewFr, self).get(request, *args, **kwargs)

class BoothDemandCreateViewEn(BoothDemandCreateView):

    def get(self, request, *args, **kwargs):
        translation.activate('en')
        request.LANGUAGE_CODE = 'en'
        return super(BoothDemandCreateViewEn, self).get(request, *args, **kwargs)

class BoothDemandCreateViewNl(BoothDemandCreateView):

    def get(self, request, *args, **kwargs):
        translation.activate('nl')
        request.LANGUAGE_CODE = 'nl'
        return super(BoothDemandCreateViewNl, self).get(request, *args, **kwargs)

