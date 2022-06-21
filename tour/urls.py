"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from home_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("dist_app/", include("dist_app.urls")),
    path("schedule_app/", include("schedule_app.urls")),
    path("",include("home_app.urls")),
    path("", views.index, name="index"),
    path("mypage_app/",include("mypage_app.urls")),
    path("board/", include("board.urls")),



    # path('dist_app/', include('dist_app.urls')),
    # path('home/', include('home_app.urls')),
    # path('mypage/', include('mypage.urls')),
    # path('recommend_app/', include('recommend_app.urls')),
    # path('schdule_app/', include('schdule_app.urls'))
]
