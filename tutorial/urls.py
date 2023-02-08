from django.urls import path, include
from . import views



app_name = 'tutorial'

urlpatterns = [
    #django
    path('index/', views.IndexView, name='home'),
    #path('test/', views.test, name='test'),
    path('blog/', views.BlogView, name='blog'),
    path('blog/<slug:slug>', views.BlogPostView, name='blog_post'),
    path('category/<slug:category_slug>/', views.CategoryView, name='category'),
    path('contact/', views.ContactView, name='contact'),
    path('portfolio/', views.PortfolioView, name='portfolio'),
    path('portfolio-item/', views.PortfolioitemView, name='portfolio-item'),
    path('ui-element/', views.UielementsView, name='ui-elements'),
    path('search/', views.SearchView, name='search'),
    path('add-comment/<slug:slug>', views.AddCommentView, name='add_comment'),
    path('add-reply-comment/', views.AddCommentView, name='add_replay_comment'),


]


