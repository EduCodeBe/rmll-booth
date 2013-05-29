from django.views.generic import CreateView
from askforabooth.models import boothDemand
from booths import settings

class BoothDemandCreateView(CreateView):
    model = boothDemand
    def get_success_url(self):
        return settings.SUCCESS_URL[self.request.LANGUAGE_CODE]

