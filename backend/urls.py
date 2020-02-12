from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [

    path('api/auth/', include('accounts.api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('challenges.api.urls')),
    path('api/ex/', include('exercises.api.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
