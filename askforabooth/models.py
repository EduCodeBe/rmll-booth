from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class boothDemand(models.Model):
    name = models.CharField(_(u'Name of the association/group/community'), max_length=64)
    start_date = models.IntegerField(_(u'Start year of the association/group/community'))
    objectives = models.TextField(_(u'Objectives and action fields'))
    members = models.IntegerField(_(u'Number of members'))
    city = models.CharField(_(u'City/state'), max_length=32)
    country = models.CharField(_(u'Country'), max_length=32)
    mail = models.EmailField(_(u'Email address'))
    internet = models.CharField(_(u'Website'), max_length=128)
    whattoshow = models.TextField(_(u'What will you show at the LSM village?'))
    sizeoftheboost = models.CharField(_(u'Which size do you need for yout boost?'), blank=True, help_text=_('We just want an estimation'), max_length=128)
    whattosell = models.TextField(_(u'What will you sell?'), help_text=_('GNU/Linux CD-ROM, t-shirts, books, stickers...'), blank=True)
    specific_needs = models.TextField(_(u'Specific needs'), help_text=_('You will have WiFi, 220V, table and chairs'), blank=True)

    def __unicode__(self):
        return self.name
