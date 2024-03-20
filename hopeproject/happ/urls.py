from . import views
from django.urls import path, include
app_name='happ'
urlpatterns = [
    path('',views.allProdcat,name="allProdCat"),
    path('<slug:c_slug>/',views.allProdcat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail')


]
