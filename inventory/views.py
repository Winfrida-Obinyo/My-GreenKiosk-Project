from django.shortcuts import render
from .forms import ProductUploadForm
from inventory.models import Product
from django.shortcuts import redirect


def upload_product(request):                     
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductUploadForm()
    return render(request, "inventory/product_upload.html", {"form": form})

def product_list(request):
    products = Product.objects.all()
    return render (request, "inventory/product_list.html", {"products": products})

def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,"inventory/product_detail.html", {"product":product})


def edit_product_view(request,id):
   product=Product.objects.get(id=id)
   if request.method=='POST':
      form=ProductUploadForm(request.POST,instance=Product)
      if form.is_valid():
         form.save()
      return redirect("product_detail_view",id=Product.id )

   else:
        form=ProductUploadForm(instance=product)
   return render (request,"edit/edit_product.html",{"form":form})
     
     