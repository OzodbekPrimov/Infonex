
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path,re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.views.static import serve

urlpatterns = i18n_patterns(
    path('admin-page-locked/', admin.site.urls),
    path('api-schema-locked/', SpectacularAPIView.as_view(), name='schema'),
    path('api-swagger-locked/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("api/", include("app.urls")),
    path('api-auth/', include('rest_framework.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# else:
#     urlpatterns += [
#         re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#         re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#     ]