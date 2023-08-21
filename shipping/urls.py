from django.urls import path
from .views import upload_shipping,shipping_list,edit_shipping_view,shipping_detail



urlpatterns = [
    path("shipping/upload", upload_shipping, name="shipping_upload_view"),
    path("shipping/list", shipping_list, name="shipping_list_view"),
    path("shipping/<int:id>/",shipping_detail,name="shipping_detail_view"),  
    path("shipping/edit/<int:id>/",edit_shipping_view,name="shipping_edit_view"),  
    
    
  
]



