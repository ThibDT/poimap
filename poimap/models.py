from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as gismodels
from django_countries.fields import CountryField
from treebeard.mp_tree import MP_Node
from polymorphic.models import PolymorphicModel

from autoslug import AutoSlugField


class Area(models.Model):
    name = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from="name", always_update=True)
    description = models.TextField(blank=True, null=True)
    geom = gismodels.PolygonField()

    @property
    def wkt(self):
        return self.geom.wkt

    def __unicode__(self):
        return self.name


class Path(MP_Node):
    name = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from="name", always_update=True)
    description = models.TextField(blank=True, null=True)
    geom = gismodels.LineStringField(dim=3)

    def __unicode__(self):
        return self.name

DEFAULT_POI_ICON_CHOICES = (
    ("flag", "Drapeau"),
    ("cutlery", "Restaurant"),
    ("bed", "Hotel"),
    ("shopping-basket", "Magasin"),
    ("tint", "Point d'eau"),
    ("certificate", "Site touristique"),
    ("exclamation", "Avertissement"),
)

icon_choices = getattr(settings, "POI_ICON_CHOICES", DEFAULT_POI_ICON_CHOICES)
poi_child_models = getattr(settings, "POI_CHILD_MODELS", [])


class POIType(models.Model):
    label = models.CharField(max_length=30)
    icon = models.CharField(max_length=30, choices=icon_choices, default="flag")

    def __unicode__(self):
        return self.label

class POI(PolymorphicModel):
    name = models.CharField(max_length=500)         # nom du point de depart - Il pourrait aussi etre un hebergement
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(POIType)

    address = models.CharField(max_length=250, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=300, blank=True, null=True)
    country = CountryField(default="FR")
    geom = gismodels.PointField(dim=3)

    @property
    def coords(self):
        return {
            "lat" : self.geom.coords[1],
            "lng" : self.geom.coords[0],
        }

    def __unicode__(self):
        return "%s - %s" % (self.name, self.type.label)

    class Meta:
        verbose_name = verbose_name_plural = "POI"
