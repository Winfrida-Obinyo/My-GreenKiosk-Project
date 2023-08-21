from django.shortcuts import render
from .forms import OrderUploadForm
from order.models import Order
from django.shortcuts import redirect


def upload_order(request):                    
    if request.method == 'POST':
        uploaded_order = request.FILES["image"]
        form = OrderUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OrderUploadForm()
    return render(request, "order/order_upload.html", {"form": form})

def order_list(request):
    order = Order.objects.all()
    return render (request, "order/order_list.html", {"orders":order})

def order_detail(request,id):
    order=Order.objects.get(id=id)
    return render(request,"order/order_detail.html", {"order":order})


def edit_order_view(request,id):
   order=Order.objects.get(id=id)
   if request.method=='POST':
      form=OrderUploadForm(request.POST,instance=Order)
      if form.is_valid():
         form.save()
      return redirect("order_detail_view",id=Order.id )

   else:
        form=OrderUploadForm(instance=order)
   return render (request,"edit/edit_order.html",{"form":form})
     
     