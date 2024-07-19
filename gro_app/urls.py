from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('index-2.html', views.index_2, name='index-2'),
    path('index-3.html', views.index_3, name='index-3'),
    path('index-4.html', views.index_4, name='index-4'),
    path('index-5.html', views.index_5, name='index-5'),
    path('index-6.html', views.index_6, name='index-6'),
    path('index-7.html', views.index_7, name='index-7'),
    path('index-8.html', views.index_8, name='index-8'),
    
    path('login-register.html', views.login, name='login-register'),
    path('shop.html', views.shop, name='shop'),
    path('shop-list.html', views.shop_list, name='shop-list'),
    path('shop-details.html', views.shop_details, name='shop-details'),
    path('cart.html', views.cart, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('wishlist.html', views.wishlist, name='wishlist'),
    path('blog.html', views.blog, name='blog'),
    path('blog-list.html', views.blog_list, name='blog-ist'),
    path('blog-grid.html', views.blog_grid, name='blog-grid'),
    path('blog-grid-sidebar.html', views.blog_grid_sidebar, name='blog-grid-sidebar'),
    path('masonry.html', views.masonry, name='masonry'),
    path('details.html', views.details, name='details'),
    path('error.html', views.error, name='error'),
    path('contact.html', views.contact, name='contact'),
]

