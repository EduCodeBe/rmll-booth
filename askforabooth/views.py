from django.views.generic import CreateView
from askforabooth.models import boothDemand
from booths import settings
from django.utils import translation



class BoothDemandCreateView(CreateView):
    model = boothDemand

    def get_success_url(self):
        return settings.SUCCESS_URL[self.request.LANGUAGE_CODE]

class BoothDemandCreateViewFr(BoothDemandCreateView):

    def post(self, request, *args, **kwargs):
        translation.activate('fr')
        request.LANGUAGE_CODE = 'fr'
        return super(BoothDemandCreateViewFr, self).post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        translation.activate('fr')
        request.LANGUAGE_CODE = 'fr'
        return super(BoothDemandCreateViewFr, self).get(request, *args, **kwargs)

class BoothDemandCreateViewEn(BoothDemandCreateView):

    def post(self, request, *args, **kwargs):
        translation.activate('en')
        request.LANGUAGE_CODE = 'en'
        return super(BoothDemandCreateViewEn, self).post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        translation.activate('en')
        request.LANGUAGE_CODE = 'en'
        return super(BoothDemandCreateViewEn, self).get(request, *args, **kwargs)

class BoothDemandCreateViewNl(BoothDemandCreateView):

    def post(self, request, *args, **kwargs):
        translation.activate('nl')
        request.LANGUAGE_CODE = 'nl'
        return super(BoothDemandCreateViewNl, self).post(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        translation.activate('nl')
        request.language_code = 'nl'
        return super(BoothDemandCreateViewNl, self).get(request, *args, **kwargs)

