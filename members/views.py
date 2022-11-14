


from http.client import HTTPResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Members, Order
from django.contrib.auth import authenticate, login
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def index(request):
    myOrders = Order.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myOrders' : myOrders,
    }
    
    

    return HttpResponse(template.render(context, request))
## Session Maker

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['title']
    y = request.POST['descrip']
    xy = request.POST['date']
    z = request.POST['price']
    order = Order(title=x, descrip=y, created=xy, price=z)
    order.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    order = Order.objects.get(id = id)
    order.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request, id):
    mymember = Members.objects.get(id = id)
    template = loader.get_template('update.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))

#register
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("base.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
