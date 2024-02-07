# from django.conf import settings
import requests
from django.db.models.fields import return_None
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Driver, Gender, Person_in_charge, Category, Transmission, Position, Trip, Brand, Division, Maintenance, List_Maintenance
from django.http import HttpResponse, Http404
from django.contrib import messages
from .forms import CarForm, CategoryForm, TransmissionForm, PositionForm,BrandForm, DivisionForm, GenderForm, DriverForm
from django.core.paginator import Paginator
#Car CRUD
def CarIndex(requests):
    if requests.method == 'GET':
        template = "car/index.html"
        data = Car.objects.all()
        page = Paginator(data, 10)
        page_list = requests.GET.get('page')
        page = page.get_page(page_list)
        return render(requests, template, {'page' : page})

def CarAdd(requests):
    #prepare template
    form = CarForm
    template = "car/add.html"
    context = {}
    #if form has request post
    if requests.method == 'POST':
        form = CarForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()
            messages.success(requests, "Success Adding Data")
            return redirect('carindex')
    context['form'] = form
    return render(requests, template, context)

def CarEdit(requests, id):
    template = "car/edit.html"
    template_detail = "car/detail.html"
    context = {}
    car = get_object_or_404(Car, id = id)
    if requests.method == 'GET':
        context = { 'form' : CarForm(instance=car), 'id':id }
        return render(requests, template, context)
    elif requests.method == 'POST':
        form = CarForm(requests.POST, requests.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(requests, "Success edit data")
            car_edit = get_object_or_404(Car, id = id)
            context  = {'car' :car_edit}
            return render(requests, template_detail, context)
        else:
            messages.error(requests, "Failed update data")
            return render(requests, template, context)

def CarDetail(requests, id):

    template = "car/detail.html"
    data = Car.objects.get(pk=id)
    context = {'car' : data }
    return render(requests, template, context)

def CarDelete(requests, id):
    car = Car.objects.get(pk = id)
    if car :
        car.delete()
        messages.success(requests,"Data delete succesfully")
        return redirect('carindex')
    else:
        messages.error(requests, "data is not exist")
        return redirect('carindex')

#Category CRUD
def CategoryIndex(requests):
    template = 'category/index.html'
    data = Category.objects.values(
        'id','category', 'created_at', 'updated_at',
    )
    context = {'category' : data}
    return render(requests, template, context)

def CategoryAdd(requests):
    form = CategoryForm
    template = "category/add.html"
    context = {}
    if requests.method == 'POST':
        form = CategoryForm(requests.POST or None)
        if form.is_valid():
            form.save()
            messages.success(requests, "Success Adding Category")
            return redirect('categoryindex')
    context['form'] = form
    return render(requests, template, context)

def CategoryEdit(requests,id):

    category = get_object_or_404(Category, id=id)

    if requests.method == 'GET':
        template = 'category/edit.html'
        context = {'form': CategoryForm(instance=category), 'id': id}
        return render(requests, template, context)

    elif requests.method == 'POST':
        form = CategoryForm(requests.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(requests, "Data edited succesfully")
            return redirect('categoryindex')
        else:
            messages.error(requests, "Edit data failed")
            return redirect('categoryindex')

def CategoryDetails(requests, id):
    template = 'category/detail.html'
    data = Category.objects.get(pk=id)
    context = {'data':data}
    return render(requests, template, context)

def CategoryDelete(requests, id):
    data = Category.objects.get(pk=id)
    data.delete()
    messages.success(requests, "Data success delete")
    return redirect('categoryindex')

#Transmission CRUD
def TransmissionIndex(request):
    template = "transmission/index.html"
    data = Transmission.objects.values('id','transmission')
    context = {'transmission': data }
    return render(request, template, context)

def TransmissionAdd(requests):
    template = "transmission/add.html"
    context = {}
    form = TransmissionForm
    if requests.method == 'POST':
        form = TransmissionForm(requests.POST or None)
        if form.is_valid():
            form.save()
            messages.success(requests, "Success adding Transmission")
            return redirect('transmissionindex')
    context['form'] = form
    return render(requests, template, context)

def TransmissionEdit(requests,id):
    transmission = get_object_or_404(Transmission, id=id)

    if requests.method == 'GET':
        template = 'transmission/edit.html'
        context = {'form' : TransmissionForm(instance=transmission), 'id':id }
        return render(requests, template, context)

    elif requests.method == 'POST':
        form = TransmissionForm(requests.POST, instance=transmission)
        if form.is_valid():
            form.save()
            messages.success(requests, "Successfull edit data")
            return redirect('transmissionindex')
        else:
            messages.error(requests, "Data failed to edit")
            return redirect('transmissionindex')

def TransmissionDetail(requests, id):
    transmission = Transmission.objects.get(pk=id)
    template = 'transmission/detail.html'
    context = {'data' : transmission}
    return render(requests, template, context)

def Transmissiondelete(requests, id):
    transmission = Transmission.objects.get(pk=id)
    transmission.delete()
    messages.success(requests, "Data deleted successfully")
    return redirect('transmissionindex')

#Position CRUD
def PositionIndex(requests):
    template = "position/index.html"
    data = Position.objects.values('id', 'code', 'position', 'created_at', 'updated_at')
    context = {'position' : data}
    return render(requests, template, context)

def PositionAdd(requests):
    form = PositionForm
    template = "position/add.html"
    context = {}
    if requests.method == 'POST':
        form = PositionForm(requests.POST or None)
        if form.is_valid():
            form.save()
            messages.success(requests, "Success adding Position")
            return redirect('positionindex')
    context['form'] = form
    return render(requests, template, context)

def PositionEdit(requests,id):
    position = get_object_or_404(Position, id=id)

    if requests.method == 'GET':
        template = 'position/edit.html'
        context = {'form' : PositionForm(instance=position), 'id':id }
        return render(requests, template, context)

    elif requests.method == 'POST':
        form = PositionForm(requests.POST, instance=position)
        if form.is_valid():
            form.save()
            messages.success(requests, "Successfull edit data")
            return redirect('positionindex')
        else:
            messages.error(requests, "Data failed to edit")
            return redirect('positionindex')

def PositionDetail(requests, id):
    position = Position.objects.get(pk=id)
    template = 'position/detail.html'
    context = {'data' : position}
    return render(requests, template, context)

def PositionDelete(requests, id):
    brand = Position.objects.get(pk=id)
    brand.delete()
    messages.success(requests, "Successfully delete data")
    return redirect('positionindex')


#Person_in_charge CRUD
#Position CRUD
#Trip CRUD
#Brand CRUD
def BrandIndex(requests):
    template = 'brand/index.html'
    brand = Brand.objects.values('id','brand', 'created_at','updated_at')
    context = {'data' : brand}
    return render(requests, template, context)

def BrandAdd(requests):
    form = BrandForm
    template = 'brand/add.html'
    context = {}
    if requests.method == 'POST':
        form = BrandForm(requests.POST or None)
        if form.is_valid():
            form.save()
            messages.success(requests, "Brand added succesfully")
            return redirect('brandindex')
    context['form'] = form
    return render(requests, template, context)

def BrandEdit(requests, id):
    brand = get_object_or_404(Brand, id=id)

    if requests.method == 'GET':
        context = {'form': BrandForm(instance=brand), 'id': id}
        return render(requests, 'brand/edit.html', context)

    elif requests.method == 'POST':
        form = BrandForm(requests.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(requests, "Brand edited succesfully")
            return redirect('brandindex')
        else:
            messages.error(requests, "Brand data failed")
            return redirect('brandindex')

def BrandDetail(requests, id):
    template = 'brand/detail.html'
    data = Brand.objects.get(pk=id)
    context = {'data' : data}
    return render(requests, template, context)

def BrandDelete(requests, id):
    brand = Brand.objects.get(pk=id)
    brand.delete()
    messages.success(requests, "Successfully delete data")
    return redirect('brandindex')

#Division CRUD
def DivisionIndex(requests):
    template = 'division/index.html'
    data = Division.objects.values('id','division', 'created_at','updated_at')
    context = {'division' : data}
    return render(requests, template, context)

def DivisionAdd(requests):
    form = DivisionForm
    template = 'division/add.html'
    context = {}
    if requests.method == 'POST':
        form = DivisionForm(requests.POST or None)
        if form.is_valid():
            form.save()
            messages.success(requests, "Division added succesfully")
            return redirect('divisionindex')
    context['form'] = form
    return render(requests, template, context)

def DivisionEdit(requests, id):
    division = get_object_or_404(Division, id=id)

    if requests.method == 'GET':
        context = {'form': DivisionForm(instance=division), 'id': id}
        return render(requests, 'division/edit.html', context)

    elif requests.method == 'POST':
        form = DivisionForm(requests.POST, instance=division)
        if form.is_valid():
            form.save()
            messages.success(requests, "Division edited succesfully")
            return redirect('divisionindex')
        else:
            messages.error(requests, "Division data failed")
            return redirect('divisionindex')

def DivisionDetail(requests, id):
    template = 'division/detail.html'
    division = Division.objects.get(pk=id)
    context = {'data' : division}
    return render(requests, template, context)

def DivisionDelete(requests, id):
    division = Division.objects.get(pk=id)
    division.delete()
    messages.success(requests, "Successfully delete data")
    return redirect('divisionindex')

#Maintenance CRUD
#List_Maintenance CRUD
#Gender CRUD

def GenderIndex(requests):
    template = 'gender/index.html'
    data = Gender.objects.values('id', 'gender', 'created_at', 'updated_at')
    context = { 'gender' : data }
    return  render(requests, template, context)

def GenderAdd(requests, id):
    template = 'gender/add.html'
    form = GenderForm
    context = {}
    if requests.method == 'POST':
        form = GenderForm(requests.POST)
        if form.is_valid():
            form.save()
            messages.success(requests, "Success adding gender")
            return redirect('genderindex')
    context['form'] = form
    return render(requests, template, context)

def GenderEdit(requests, id):
    gender = get_object_or_404(Gender, id = id)
    template = 'gender/edit.html'
    if requests.method == 'GET':
        context = {'form' : GenderForm(instance=gender) , 'id' : id}
        return render(requests, template, context)
    elif requests.method == 'POST':
        form = GenderForm(requests.POST, instance=gender)
        if form.is_valid():
            form.save()
            messages.success(requests, "Gender has Updated")
            return redirect('genderindex')
        else:
            messages.error(requests, "Data failed to edit")
            return render(requests, template, context)

def GenderDetail(requests, id):
    gender = get_object_or_404(Gender, id=id)
    template = 'gender/detail.html'
    context = {'data' : gender}
    return render(requests, template, context)

def GenderDelete(requests, id):
    gender = Gender.objects.get(pk=id)
    gender.remove()
    messages.success(requests, "Gender has remove")
    return redirect('genderindex')

def DriverIndex(requests):
    if requests.method == 'GET':
        data = Driver.objects.values(
        'id','name', 'driving_lisence_number', 'image_driving_lisence' , 'birth', 'identity_number', 'image_identity_number', 'created_at', 'updated_at', 'gender_id',
        )
        template = 'driver/index.html'
        if data :
            context = {'driver' : data}
            return render(requests, template, context)
        else:
            return render(requests, template, {'messages' : "data doesn't exist"})


def DriverAdd(requests):
    form = DriverForm
    template = 'driver/add.html'
    context = {}
    if requests.method == 'POST':
        form = DriverForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()
            messages.success(requests, "Success addedd Driver")
            return redirect('driverindex')
    context['form'] = form
    return render(requests, template, context)
    # return HttpResponse(form)
def DriverEdit(requests, id):
    driver = get_object_or_404(Driver, id = id)
    template = 'driver/edit.html'
    if requests.method == 'POST':
        form = DriverForm(requests.POST,requests.FILES, instance=driver)
        if form.is_valid():
            form.save()
            messages.success(requests, "Success edit data driver")
            return redirect('driverindex')
        else:
            messages.error(requests, "Data failed to update, please check again")
            return redirect('driverindex')
    if requests.method == 'GET':
        context = {'form':DriverForm(instance=driver), 'id':id}
        return render(requests, template, context)

def DriverDetail(requests, id):
    driver = Driver.objects.get(pk = id)
    template = 'driver/detail.html'
    context = {'data'  : driver}
    return render(requests, template, context)

def DriverDelete(requests, id):
    driver = Driver.objects.get(pk = id)
    driver.remove()
    messages.success(requests, "Success delete data")
    return redirect('driverindex')

# Car, Driver, Gender, Person_in_charge, Category, Transmission, Position, Trip, Brand, Division, Maintenance, List_Maintenance