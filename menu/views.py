from django.shortcuts import render
from .models import Category, MenuItem

def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'menu/index.html', context)

def category_menu(request, category_id):
    category = Category.objects.get(pk=category_id)
    menu_items = MenuItem.objects.filter(category=category)
    context = {'category': category, 'menu_items': menu_items}
    return render(request, 'menu/category_menu.html', context)

def item_details(request, item_id):
    menu_item = MenuItem.objects.get(pk=item_id)
    context = {'menu_item': menu_item}
    return render(request, 'menu/item_details.html', context)

def main_page(request):
    return render(request, 'menu/main_page.html')


def dinner(request):
    return render(request, 'menu/dinner.html')

def brunch(request):
    return render(request, 'menu/brunch.html')

def dessert(request):
    return render(request, 'menu/dessert.html')

def drinks(request):
    return render(request, 'menu/drinks.html')

def omelette(request):
    return render(request, 'menu/omlette.html')
def smoothie(request):
    return render(request, 'menu/smoothie.html')

def oatmeal(request):
    return render(request, 'menu/oatmeal.html')

def chia(request):
    return render(request, 'menu/chia.html')

