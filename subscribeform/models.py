from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class boothDemand(models.Model):
    first_name = models.CharField(_(u'First name'), max_length=64)
    last_name = models.CharField(_(u'Last name'), max_length=64)
    birth_date = models.DateField(_(u'Birth date'), help_text=_(u'YYYY-MM-DD'))
    mail = models.EmailField(_(u'Email address'))

    def __unicode__(self):
        return self.first_name
