from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import view_listings, listing , search
from django.views.static import serve

urlpatterns = [
    path ('', view_listings , name='listings'),
    path ('<int:listing_id>', listing , name='listing'),
    path ('search', search , name='search')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)