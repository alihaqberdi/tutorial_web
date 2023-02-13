from django.db.models import Q
from django.shortcuts import render
from .models import Product, Category, Commentary
from django.core.paginator import Paginator
from accounts.models import CustomUser
from django.shortcuts import redirect


# Create your views here.

def BlogView(request):
    context = Product.objects.filter(is_activated=True)
    # Paginator
    p = Paginator(context, 6)
    page = request.GET.get('page')
    product = p.get_page(page)
    all = Category.objects.all()
    context = {
         'product': product,
         'context': context,
         'category': all
    }
    return render(request, 'blog.html', context)


def CategoryView(request, category_slug=None):
    category_ism = Category.objects.get(slug=category_slug)
    context = Product.objects.filter(is_activated=True)
    # Paginator
    p = Paginator(Product.objects.filter(Q(category=category_ism) & Q(is_activated=True)), 6)
    page = request.GET.get('page')
    product = p.get_page(page)
    all = Category.objects.all()
    context= {
        'product': product,
         'category_name': category_ism,
         'context': context,
         'category': all
    }
    return render(request, 'blog.html', context)


def BlogPostView(request, slug=None):
    context = Product.objects.filter(is_activated=True)
    detail = Product.objects.get(slug=slug)
    obj = Commentary.objects.filter(product__slug=slug)
    all = Category.objects.all()
    context ={
        'detail': detail,
        'commentary': obj,
        'context': context,
        'category': all
    }
    return render(request, 'blog-post.html', context)


def ContactView(request):
    return render(request,'contact.html')


def SearchView(request):
    context = Product.objects.filter(is_activated=True)
    query = request.GET.get('texting')
    product = Product.objects.filter(Q(title__icontains=query) | Q(discription__icontains=query))
    all = Category.objects.all()
    context = {'product': product,
               'category': all,
               'context': context}
    return render(request, 'blog.html', context)


def AddCommentView(request, slug):
    #add comment
    text = request.GET.get('add_comment')
    user = CustomUser.objects.get(username=request.user.username)
    product = Product.objects.get(slug=slug)
    add = Commentary(product_id=int(product.id), author_id=int(user.id), text=text)
    add.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))










