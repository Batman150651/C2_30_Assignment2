from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),  # Routes the homepage to app1
    path('app2/', include('app2.urls')),  # Routes /app2/sample/ to app2
]
