from django.urls import path
from . import views
urlpatterns = [
    path('device/', views.index, name='device'),
    path(
        'api/device/(?P<pk>[0-9]+)',
        views.get_delete_update_device,
        name='get_delete_update_device'
    ),
    path(
        'api/device/',
        views.get_post_device,
        name='get_post_device'
    ),
    ]
