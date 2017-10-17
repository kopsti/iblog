from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from registration.backends.hmac.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',  RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='auth_signup'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^', include("posts.urls", namespace='posts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
