from django.shortcuts import render

# Create your views here.
def store(request):
	context = {}
	return render(request,'fontend/store.html',context)

def cart(request):
	context = {}
	return render(request,'fontend/cart.html',context)

def checkout(request):
	context = {}
	return render(request,'fontend/checkout.html',context)

def detail(request):
	context = {}
	return render(request,'fontend/detail.html',context)

def login(request):
	context = {}
	return render(request,'fontend/login.html',context)

def register(request):
	context = {}
	return render(request,'fontend/register.html',context)

