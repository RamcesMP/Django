from django.urls import path
from .views import home

#Para trabajar con imagenes es necesario cargar los media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home , name="home" ),
]

#Para trabajar con imagenes es necesario cargar los media
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
