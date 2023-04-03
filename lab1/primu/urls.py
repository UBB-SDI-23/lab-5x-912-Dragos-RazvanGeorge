"""primu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from primu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/',views.CarApiView.as_view()),
    path('cars/<int:id>',views.CarDetailView.as_view()),
    path('rims/',views.RimsApiView.as_view()),
    path('racetracks/',views.RaceTracksApiView.as_view()),
    path('rims/<int:id>',views.RimsDetailApiView.as_view()),
    path('racetracks/<int:id>',views.RaceTrackDetailApiView.as_view()),
    path('owners/',views.OwnersApiView.as_view()),
    path('ownerscars/',views.OwnersCarsApiView.as_view()),
    path('owners/<int:id>',views.OwnersDetailView.as_view()),
    path('ownerscars/<int:id>',views.OwnersCarsDetailApiView.as_view()),
    path('car_owner_report/',views.CarOwnerReport1ApiView.as_view(), name='car_owner_report'),
    path("multiplecarbrand/", views.MultipleRimsCarView.as_view()),
    path('car_rims_report/',views.CarRimsReport1ApiView.as_view(), name='car_rims_report')
]
