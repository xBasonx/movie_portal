from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmy/', include('filmyweb.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),#połączenie dwóch adresów url , wyświetlanie loginu gdy sie wylogujemy
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from filmyweb.views import test_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response )
]

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmy/', include('filmyweb.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
