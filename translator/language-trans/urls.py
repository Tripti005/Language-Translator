from django.urls import path
from language_trans.views import image_view


urlpatterns = [
    path('', image_view, name='image_upload'),
]

