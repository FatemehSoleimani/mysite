from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.from django.http import HttpResponse
def index_view(request):
    return render(request,'website/index.html')
def shop_view(request):
    return  render(request,'website/shop.html')
def contact_view(request):
    return  render(request,'website/contact.html')