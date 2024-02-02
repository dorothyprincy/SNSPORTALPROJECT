def Login_Page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User Does Not Exist !')
        try:
            vendor_authe = User_login.objects.get(user_auth=user, is_vendor_user='y',is_customer_user='n')
            user = authenticate(request, username= username, password = password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request,'Username and Password Does Not Match. !')
        except:
            messages.error(request,'User not Found !')
       
    else:
        pass
    context = {

    }
    return render(request,'panel/login.html',context)


# Create your views here
def User_Login_Page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,'User Does Not Exist !')
        try:
            user_authe = User_login.objects.get(user_auth=user, is_vendor_user='n',is_customer_user='y')
            user = authenticate(request, username= username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,'Username and Password Does Not Match. !')
        except:
            messages.error(request,'User not Found !')
    else:
        pass
    context = {
        'form_type':'user_login'
    }
    return render(request,'base/login.html', context)


#Here base app urls.py

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('user-login/', views.User_Login_Page, name="user_login"),
    path('user-registration/', views.User_Registration, name="user_registration"),
    path('user-logout/', views.User_Logout, name="user_logout"), 
   
    path('', views.HomePage, name="home"),
]

#Here panel app urls.py

from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('', views.Login_Page, name="login_page"),
    path('logout/', views.Vendor_logout, name="logout_page"),
    
    path('dashbord/', views.Dashboard_Page, name="dashboard"),
]