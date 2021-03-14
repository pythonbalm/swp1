from django.conf.urls import include, url

from django.contrib import admin
from qa.views import test
admin.autodiscover()

urlpatterns = [

    url(r'^$', test),

    url(r'^init25/', test),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^ask/', test),
    # url(r'^answer/', answer),
    url(r'^popular/', test),
    url(r'^new/', test),

    url(r'^admin/', admin.site.urls),
    url(r'^question/', include('qa.urls')),

    url(r'^', not_found),
]
