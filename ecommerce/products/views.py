from django.views.generic import ListView,DetailView,TemplateView
from django.shortcuts import render
from .models import Product

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"

class DetailListView(DetailView):
    model = Product
    template_name = "products/detail.html"  

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()
  
    
  