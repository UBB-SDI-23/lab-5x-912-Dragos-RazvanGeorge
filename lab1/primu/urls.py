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
    path('cars/<int:id>',views.car_detail),
    path('rims/',views.rims_list),
    path('racetracks/',views.racetracks_list),
    path('rims/<int:id>',views.rims_detail),
    path('racetracks/<int:id>',views.racetracks_detail),
    path('owners/',views.owners_list),
    path('ownerscars/',views.ownersCars_list),
    path('owners/<int:id>',views.owners_detail),
    path('ownerscars/<int:id>',views.ownersCars_detail),
    path('car_owner_report/',views.car_owner_report1, name='car_owner_report'),
    path("multiplecarbrand/", views.MultipleRimsCarView.bulkAdd),
    path('car_rims_report/',views.car_rims_report1, name='car_rims_report')
]
