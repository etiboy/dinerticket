from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def index(request):
	#returning all restaurant object in a restaurants context, which can be accessed in the index.html file. Yes o.
	return render(request,'index.html',{'restaurants': Restaurant.objects.all()})