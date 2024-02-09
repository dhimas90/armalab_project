from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # car not fix
    path("", views.CarIndex, name='carindex'),
    path("caradd/", views.CarAdd, name='caradd'),
    path("caredit/<int:id>", views.CarEdit, name='caredit'),
    path("cardetail/<int:id>", views.CarDetail, name='cardetail'),
    path("cardelete/<int:id>", views.CarDelete, name='cardelete'),
    # category ok
    path("category/", views.CategoryIndex, name='categoryindex'),
    path("categoryadd/", views.CategoryAdd, name='categoryadd'),
    path("categoryedit/<int:id>", views.CategoryEdit, name='categoryedit'),
    path("categorydetail/<int:id>", views.CategoryDetails, name='categorydetail'),
    path("categorydelete/<int:id>", views.CategoryDelete, name='categorydelete'),
    # brand ok

    path("brand/", views.BrandIndex, name='brandindex'),
    path("brandadd/", views.BrandAdd, name='brandadd'),
    path("brandedit/<int:id>", views.BrandEdit, name='brandedit'),
    path("branddetail/<int:id>", views.BrandDetail, name='branddetail'),
    path("branddelete/<int:id>", views.BrandDelete, name='branddelete'),

    path("transmission/", views.TransmissionIndex, name='transmissionindex'),
    path("transmissionadd/", views.TransmissionAdd, name='transmissionadd'),
    path("transmissionedit/<int:id>", views.TransmissionEdit, name='transmissionedit'),
    path("transmissiondetail/<int:id>", views.TransmissionDetail, name='transmissiondetail'),
    path("transmissiondelete/<int:id>", views.Transmissiondelete, name='transmissiondelete'),

    path("position/", views.PositionIndex, name='positionindex'),
    path("positionadd/", views.PositionAdd, name='positionadd'),
    path("positionedit/<int:id>", views.PositionEdit, name='positionedit'),
    path("positiondetail/<int:id>", views.PositionDetail, name='positiondetail'),
    path("positiondelete/<int:id>", views.PositionDelete, name='positiondelete'),

    path("gender/", views.GenderIndex, name='genderindex'),
    path("genderadd/", views.GenderAdd, name='genderadd'),
    path("genderedit/<int:id>", views.GenderEdit, name='genderedit'),
    path("genderdetail/<int:id>", views.GenderDetail, name='genderdetail'),
    path("genderdelete/<int:id>", views.GenderDelete, name='genderdelete'),

    path("division/", views.DivisionIndex, name='divisionindex'),
    path("divisionadd/", views.DivisionAdd, name='divisionadd'),
    path("divisionedit/<int:id>", views.DivisionEdit, name='divisionedit'),
    path("divisiondetail/<int:id>", views.DivisionDetail, name='divisiondetail'),
    path("divisiondelete/<int:id>", views.DivisionDelete, name='divisiondelete'),

    path("driver/", views.DriverIndex, name='driverindex'),
    path("driveradd/", views.DriverAdd, name='driveradd'),
    path("driveredit/<int:id>", views.DriverEdit, name='driveredit'),
    path("driverdetail/<int:id>", views.DriverDetail, name='driverdetail'),
    path("driverdelete/<int:id>", views.DriverDelete, name='driverdelete'),

    path('serialcar/', views.Restcar, name="carrestdata")
]














