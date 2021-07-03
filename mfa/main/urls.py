from django.urls import path
from .views import test_view, ProductDetailView, ourdt, lucoshko

urlpatterns = [
    path('', test_view, name='base'),
    path('<str:ct_model>/<slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('ourdt', ourdt, name='ourdt'),
    path('lucoshko', lucoshko, name='lucoshko'),

]