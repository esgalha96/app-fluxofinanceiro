from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acesso/', include('django.contrib.auth.urls')),
    path('acesso/', include('acesso.urls')),
    path('', include('page.urls'))
]
