from django.conf.urls import url
from .api_views import StopListView, LineListView, api_route_timetable, api_itinerary

urlpatterns = [
    url(r'^stop/list$', StopListView.as_view(), name='api-stop-list'),
    url(r'^line/list$', LineListView.as_view(), name='api-line-list'),
    url(r'^service/list$', api_route_timetable, name='api-route-timetable'),
    url(r'^itinerary$', api_itinerary, name='api-itinerary'),
]
