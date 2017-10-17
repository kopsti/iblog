from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration.backends.hmac.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="pages/index.html"), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name="pages/about.html"), name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$',  RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='auth_signup'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^blog/', include("posts.urls", namespace='posts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
