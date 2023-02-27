from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from filmyweb.views import test_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response )
]
=======
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmy/', include('filmyweb.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 422b0396 (003. Nowe szablony, edycja filmu)
