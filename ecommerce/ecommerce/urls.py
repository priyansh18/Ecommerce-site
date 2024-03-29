"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from .views import home_page,about_page,contact_page,login_page
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_page,name='home'),
    url(r'^about/$',about_page,name='about'),
    url(r'^products/',include(('products.urls','products'),namespace='product')),
    url(r'^search/',include(('search.urls','search'),namespace='search' )),
    url(r'^login/$',login_page,name='login'),
    url(r'^contact/$',contact_page,name='contact'),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)