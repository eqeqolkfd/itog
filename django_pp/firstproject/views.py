from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Tag
from .forms import ProductForm, CategoryForm
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def info_view(request):
    return render(request, 'info.html')


@login_required
def account_view(request):
    return render(request, 'account.html')

@login_required
def cart_view(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    return render(request, 'cart.html', {'products': products})


@login_required
def catalog_view(request):
    products = Product.objects.filter(is_deleted=False)
    return render(request, 'catalog.html', {'products': products})

@login_required
def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
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

@login_required
def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def category_products_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.filter(is_deleted=False)
    return render(request, 'category_products.html', {'category': category, 'products': products})

@login_required
@permission_required('firstproject.add_product', raise_exception=True)
def add_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@login_required
def tag_list_view(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})

@login_required
def tag_products_view(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    products = tag.products.filter(is_deleted=False)
    return render(request, 'tag_products.html', {'tag': tag, 'products': products})

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart.append(product_id)
    request.session['cart'] = cart
    return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        request.session['cart'] = cart
    return redirect('cart')

@login_required
def order_view(request):
    if request.method == 'POST':
        request.session['cart'] = []
        messages.success(request, 'Заказ оформлен!')
        return redirect('cart')
    return redirect('catalog')

@login_required
@permission_required('firstproject.add_product', raise_exception=True)
def delete_category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('category_list')

@login_required
@permission_required('firstproject.add_product', raise_exception=True)
def edit_category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form, 'category': category})

@login_required
@permission_required('firstproject.add_product', raise_exception=True)
def edit_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('productdetail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

@login_required
@permission_required('firstproject.add_product', raise_exception=True)
def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('catalog')
    return render(request, 'confirm_delete_product.html', {'product': product})



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user, role = form.save()
            group = Group.objects.get(name=role)
            user.groups.add(group)
            login(request, user)
            return redirect('catalog')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('catalog')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('register')
