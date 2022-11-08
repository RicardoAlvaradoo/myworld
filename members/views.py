


from http.client import HTTPResponse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Members, Order

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


