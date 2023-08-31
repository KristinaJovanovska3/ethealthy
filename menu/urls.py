from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_menu, name='category_menu'),
    path('item/<int:item_id>/', views.item_details, name='item_details'),
    path('', views.main_page, name='main_page'),
    path('', views.brunch, name='brunch'),
    path('', views.dinner, name='dinner'),
    path('', views.dessert, name='dessert'),
    path('', views.drinks, name='drinks'),
    path('', views.omelette, name='omelette'),
    path('', views.smoothie, name='smoothie'),
    path('', views.chia, name='chia'),
    path('', views.oatmeal, name='oatmeal'),

]
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
