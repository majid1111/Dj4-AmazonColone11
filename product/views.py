from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from.models import Product , ProductImages , Brand , Review



# Create your views here.

class ProductList(ListView):
    model = Product



class ProductDetail(DetailView):
    model = Product   


    def get_context_data(self , **kwargs):
     context = super().get_context_data(**kwargs)
     context["reviews"]=Review.objects.filter(product =self.get_object())
     context["related_products"]= Product.objects.filter(brand=self.get_object().brand)
     return context  
    



class BrandList(ListView):
   model = Brand    



class BrandDetail(ListView) :
   model = Product
   template_name ='product/brand_detail.html' 
   paginate_by = 20


   def get_queryset(self) :
      brand = Brand.objects.get(slug =self.kwargs['slug'])
      return super().get_queryset().filter(brand=brand)
   


   def get_context_data(self, **kwargs) :
      context=super().get_context_data(**kwargs)
      context["brand"]= Brand.objects.get(slug =self.kwargs['slug'])
      return context
   


# def brand_list(request) :
#    brands = Brand.objects.all() 
#    context = {'data:brands'} 
#    return render(request,'brands.html', context)