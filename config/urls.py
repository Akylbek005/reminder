from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Reminders API",
        default_version='1.0 version',
        description="On test server",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="iakylbek005@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('reminders/', include('reminders.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
