from django.db.models import Q
from django.shortcuts import render
from .models import Product, Category, Commentary
from django.core.paginator import Paginator
from accounts.models import CustomUser
from django.urls import reverse
# Create your views here.


def IndexView(request):
    return render(request,'index.html')


def BlogView(request):
    context = Product.objects.filter(is_activated=True)
    # Paginator
    p = Paginator(context, 3)
    page = request.GET.get('page')
    product = p.get_page(page)
    all = Category.objects.all()
    for i in product:
        print(i.author)
    return render(request, 'blog.html', {'product': product,
                                        'context': context,
                                        'category': all})


def CategoryView(request, category_slug=None):
    category_ism = Category.objects.get(slug=category_slug)
    context = Product.objects.filter(is_activated=True)
    # Paginator
    p = Paginator(Product.objects.filter(Q(category=category_ism) & Q(is_activated=True)), 3)
    page = request.GET.get('page')
    product = p.get_page(page)
    all = Category.objects.all()
    return render(request, 'blog.html', {'product': product,
                                         'category_name': category_ism,
                                         'context': context,
                                         'category': all})


def BlogPostView(request, slug=None):
    context = Product.objects.filter(is_activated=True)
    detail = Product.objects.get(slug=slug)
    obj = Commentary.objects.filter(product__slug=slug)
    all = Category.objects.all()
    return render(request, 'blog-post.html', context={'detail': detail,
                                              'commentary': obj,
                                              'context': context,
                                              'category': all})


def UielementsView(request):
    return render(request,'ui-elements.html')


def PortfolioView(request):
    return render(request,'portfolio.html')


def PortfolioitemView(request):
    return render(request,'portfolio-item.html')


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
    user = CustomUser.objects.filter(username=request.user.username)
    product = Product.objects.filter(slug=slug)
    add = Commentary(product_id=int(product[0].id), author_id=user[0].id, text=text)
    add.save()
    return render(request, 'blog-post.html', {'detail': product})









