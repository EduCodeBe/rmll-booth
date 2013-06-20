from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class boothDemand(models.Model):
    first_name = models.CharField(_(u'First name'), max_length=64)
    last_name = models.CharField(_(u'Last name'), max_length=64)
    birth_date = models.IntegerField(_(u'Birth date'))
    mail = models.EmailField(_(u'Email address'))

    def __unicode__(self):
        return self.name
