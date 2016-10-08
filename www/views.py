from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def index(request):

	return render(request,'index.html',{'restaurants': Restaurant.objects.all()})