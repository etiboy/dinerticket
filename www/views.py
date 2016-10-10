from django.shortcuts import render
from .models import Restaurant
from django.views import generic
# Create your views here.
#def index(request):
	#returning all restaurant object in a restaurants context, which can be accessed in the index.html file. Yes o.
#	return render(request,'index.html',{'restaurants': Restaurant.objects.all()})

class IndexView(generic.ListView):
	template_name = "index.html"
	context_object_name = "restaurants"

	def get_queryset(self):
		return Restaurant.objects.all()

class RestaurantView(generic.DetailView):
	model = Restaurant
	template_name = "restaurant.html"