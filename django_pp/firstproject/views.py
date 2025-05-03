from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Tag
from .forms import ProductForm, CategoryForm

def info_view(request):
    return render(request, 'info.html')

def feedback_view(request):
    return render(request, 'feedback.html')

def api_view(request):
    return render(request, 'api.html')

def account_view(request):
    return render(request, 'account.html')

def cart_view(request):
    return render(request, 'cart.html')


def catalog_view(request):
    products = Product.objects.filter(is_deleted=False)
    return render(request, 'catalog.html', {'products': products})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {
        'form': form
        })

def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.filter(is_deleted=False)
    return render(request, 'category_products.html', {'category': category, 'products': products})


def add_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


def tag_list_view(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})

def tag_products_view(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    products = tag.products.filter(is_deleted=False)
    return render(request, 'tag_products.html', {'tag': tag, 'products': products})
