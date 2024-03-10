"""
URL configuration for BankApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from InfinityFinance import views as infinity_views  # Import the views from InfinityFinance app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', infinity_views.home, name=''),  # Use infinity_views to access the views
    path('account/', infinity_views.account, name='account'),
    path('transfer/', infinity_views.transfer, name='transfer'),
    path('deposit/', infinity_views.deposit, name='deposit'),
    path('withdraw/', infinity_views.withdraw, name='withdraw'),
    path('register/', infinity_views.RegisterView.as_view(), name="signup"),
    path('account/<int:account_id>/', infinity_views.account_details, name="account_details"),
]

handler404 = 'InfinityFinance.views.error_404'  # Correct the handler404 to use the correct module path
