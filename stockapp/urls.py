from django.urls import path
from .views import * 


urlpatterns = [
    path('warehouse-list',WarehouseListAPIView.as_view()),
    path('warehouse-create',WarehouseCreateAPIView.as_view()),
    path('warehouse-retrieve/<str:pk>',WarehouseRetrieveAPIView.as_view()),
    path('warehouse-rud/<str:pk>',WarehouseRUDAPIView.as_view()),

    path('product-list',ProductListAPIView.as_view()),
    path('product-create',ProductCreateAPIView.as_view()),
    path('product-retrieve/<str:pk>',ProductRetrieveAPIView.as_view()),
    path('product-rud/<str:pk>',ProductRUDAPIView.as_view()),

    path('customer-list',CustomerListAPIView.as_view()),
    path('customer-create',CustomerCreateAPIView.as_view()),
    path('customer-retrieve/<str:pk>',CustomerRetrieveAPIView.as_view()),
    path('customer-rud/<str:pk>',CustomerRUDAPIView.as_view()),

    path('shipment-list',ShipmentListAPIView.as_view()),
    path('shipment-cerate',ShipmentCreateAPIView.as_view()),
    path('shipment-retrieve/<str:pk>',ShipmentRetrieveAPIView.as_view()),
    path('shipment-rud/<str:pk>',ShipmentRUDAPIView.as_view()),
]


