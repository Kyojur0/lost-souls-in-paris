"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


"""

    What this code means is that whenever django encounters `/` it will send the URL 
    to the `urls.py` file of the `ecommerceapp` app. And whenever it encounters URL 
    that begins with `/authapp/` it will send the URL to the `urls.py` file of the
    `authapp` app. And whenever it encounters URL that begins with `/admin/` it will
    send the URL to the default django admin page.
    
    The `+ static` part is used to serve the static files of the project. It only 
    tells the django that media files of the project are located in the `MEDIA_ROOT`
    directory. And it tells the django that the static files of the project are located
    in the `STATIC_ROOT` directory. And it tells the django that the URL for the media
    files is `MEDIA_URL` and the URL for the static files is `STATIC_URL`.
    
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerceapp.urls', namespace='ecomapp')),
    path('authapp/', include('authapp.urls', namespace='authapp')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
