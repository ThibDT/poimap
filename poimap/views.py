from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.gis.geos import Polygon
from django.views.generic import TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from copy import deepcopy
from rest_framework import generics

from .serializers import PathSerializer, POISerializer, TypedPOISerializer, AreaSerializer
from .models import Path, POI, POIType, Area


class AreaView(generics.RetrieveAPIView):
    queryset = Area.objects.all()
    lookup_field = 'slug'
    serializer_class = AreaSerializer


class PathView(generics.RetrieveAPIView):
    queryset = Path.objects.all()
    lookup_field = 'slug'
    serializer_class = PathSerializer


class SubPathListView(generics.ListAPIView):
    serializer_class = PathSerializer

    def get_queryset(self):
        area = get_object_or_404(Area, slug=self.kwargs["slug"])
        root_path = Path.get_root_nodes().get(geom__within=area.geom)
        return root_path.get_descendants()


class AreaPathsView(generics.ListAPIView):
    serializer_class = PathSerializer

    def get_queryset(self):
        area = get_object_or_404(Area, slug=self.kwargs["slug"])
        queryset = Path.objects.filter(geom__within=area.geom)
        bbox_param = self.request.query_params.get('bbox', None)
        if bbox_param:
            bbox_param = [float(x) for x in bbox_param.split(',')]
            xmin = bbox_param[0]
            ymin = bbox_param[1]
            xmax = bbox_param[2]
            ymax = bbox_param[3]
            bbox = Polygon.from_bbox((xmin, ymin, xmax, ymax))
            queryset = queryset.filter(geom__contained=bbox)
        return queryset

class POIList(generics.ListAPIView):
    serializer_class = POISerializer

    def get_queryset(self):
        queryset = POI.objects.all()
        if 'pk' in self.kwargs:
            queryset = queryset.filter(id=self.kwargs['pk'])

        bbox_param = self.request.query_params.get('bbox', None)
        if bbox_param:
            bbox_param = [float(x) for x in bbox_param.split(',')]
            xmin = bbox_param[0]
            ymin = bbox_param[1]
            xmax = bbox_param[2]
            ymax = bbox_param[3]
            bbox = Polygon.from_bbox((xmin, ymin, xmax, ymax))
            queryset = queryset.filter(geom__contained=bbox)
        return queryset

class MapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        context.update({
            'area_slug' : kwargs["area_slug"]
        })
        return context


@login_required
@staff_member_required
def convert_poi(request, pk, to_model):
    poi = POI.objects.get(id=pk)
    target_ct = ContentType.objects.get(model=to_model)
    target = target_ct.model_class().objects.create(poi_ptr_id=poi.id, name=poi.name, type=poi.type, geom=poi.geom)
    return redirect("admin:%s_%s_change" % (target_ct.app_label, target_ct.model), target.id)
