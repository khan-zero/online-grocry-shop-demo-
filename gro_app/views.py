from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
   
def index_2(request):
    return render(request, 'index-2.html')   
     
def index_3(request):
    return render(request, 'index-3.html')
    
def index_4(request):
    return render(request, 'index-4.html')    
    
def index_5(request):
    return render(request, 'index-5.html')    
    
def index_6(request):
    return render(request, 'index-6.html')    
    
def index_7(request):
    return render(request, 'index-7.html')
    
def index_8(request):
    return render(request, 'index-8.html')
    
    
    

def login(request):
    return render(request, 'login-register.html')
    
def shop(request):
    return render(request, 'shop.html')
    
def shop_list(request):
    return render(request, 'shop_list.html') 
    
def shop_details(request):
    return render(request, 'shop_details.html')
    
def cart(request):
    return render(request, 'cart.html') 
    
def checkout(request):
    return render(request, 'checkout.html')
    
def wishlist(request):
    return render(request, 'wishlist.html')
    
def blog(request):
    return render(request, 'blog.html')
    
def blog_list(request):
    return render(request, 'blog-list.html')    
    
def blog_grid(request):
    return render(request, 'blog-grid.html')   
    
def blog_grid_sidebar(request):
    return render(request, 'blog-grid-sidebar.html')        

def masonry(request):
    return render(request, 'masonry.html')

def details(request):
    return render(request, 'details.html')
    
def error(request):
    return render(request, 'error.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') #muoffaqeatdan so'ng index.htmlga qaytish 
        else:
            messages.error(request, 'Invalid username or password.') #agar biror muammoga duch kelsa xabar yuborish
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    return render(request, 'login.html')
     
     
