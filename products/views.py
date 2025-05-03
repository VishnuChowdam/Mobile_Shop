from django.shortcuts import render
from .models import phones
from http.client import HTTPResponse
from django.shortcuts import render
from .models import customuser,phones
from django.http import HttpResponse
# Create your views here.
def product_list(request):
    p = phones.objects.all()[:4]
    return render(request, "index.html", {'phones': p,"check":0})
def sign_up(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if customuser.objects.filter(name=name).exists():
            return render(request, 'register.html', {"msg": "User already exists"})
        us=customuser(name=name, password=password)
        us.save()
        return render(request, "base.html", {"check": 1, "customusername": name})
    return render(request, "base.html", {"check": 0})
def sign_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = customuser.objects.filter(name=name).first()
        if user:
            if user.password == password:
                return render(request, 'base.html', {"check": 1, "username": name})
            else:
                return render(request, 'login.html', {"msg": "Password not matched", "check": 0})
        else:
            return render(request, 'login.html', {"msg": "User does not exist", "check": 0})
    return render(request, "login.html", {"check": 0})
def compare(request):
    if(request.method=="GET"):
        mobile1=request.GET.get('mobile1')
        mobile2=request.GET.get('mobile2')
        m1 = phones.objects.filter(model=mobile1).first()
        m2 = phones.objects.filter(model=mobile2).first()
        if (m1 == None and m2 == None):
            return render(request, "search.html", {"msg": "Mobiles does not exist"})
        elif(m1==None):
            return render(request,"search.html",{"msg":"Mobile1 does not exist"})
        elif(m2==None):
            return render(request, "search.html", {"msg": "Mobile2 does not exist"})
        return render(request,"show.html",{"m1":m1,"m2":m2})
    return render(request,"index.html")
def view_all(request):
    m=phones.objects.all()
    return render(request,"products.html",{"phones":m})
def filter(request):
    if request.method == "POST":
        brand = request.POST.get('brand') or None
        ram = request.POST.get('ram') or None
        storage = request.POST.get('storage') or None
        price = request.POST.get('price') or None
        filters = {}
        if brand and brand != 'select':
            filters['brand'] = brand
        if ram and ram != 'select':
            filters['ram'] = ram
        if storage and storage != 'select':
            filters['storage_capacity'] = storage
        if price and price != 'select':
            if '-' in price:
                min_price, max_price = price.split('-')
                filters['price__gte'] = int(min_price)
                filters['price__lte'] = int(max_price)
            elif price.endswith('+'):
                filters['price__gte'] = int(price.rstrip('+'))
            elif price.isdigit():
                filters['price__lte'] = int(price)
        results = phones.objects.filter(**filters)
        if results.exists():
            return render(request, "products.html", {"phones": results})
        else:
            return render(request, "products.html", {"msg": "No matching phones found."})
    return render(request, "products.html")
def product_search(request):
    if request.method=="GET":
        mobile=request.GET.get('phone')
        mobile = ' '.join(word.capitalize() if word.isalpha() else word for word in mobile.split())
        m=phones.objects.filter(model=mobile).first()
        if(m):
            return render(request,'model_display.html',{"m":m})
        else:
            return render(request,'model_display.html',{"msg":"No such model is present"})
    return render(request,"model_display.html")

# Create your views here.
