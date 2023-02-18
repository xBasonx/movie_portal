from django.contrib import admin
from django.urls import path
from filmyweb.views import test_response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_response )
]
