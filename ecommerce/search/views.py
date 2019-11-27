from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from products.models import Product


# Create your views here.


class SearchListView(ListView):
    model = Product
    template_name = "search/view.html"

    def get_queryset(self, *args,**kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None :
            return Product.objects.filter(Title__icontains=query)    
        return Product.objects.none()


