from django.conf.urls import include, url
from django.contrib import admin
from paytm.views import response 
urlpatterns = [
    # Examples:
    # url(r'^$', 'payments.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^paytm/', include('paytm.urls')),
    url(r'^admin/', include(admin.site.urls)),	
    url(r'^en-us/callback/', response)	
]
