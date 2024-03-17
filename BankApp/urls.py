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
    path('admin/', admin.site.urls, name='admin'),
    path('', infinity_views.home, name='home'),
    #path('account/', infinity_views.account, name='account'),
    #path('transfer/', infinity_views.transfer, name='transfer'),
    #path('deposit/', infinity_views.deposit, name='deposit'),
    #path('withdraw/', infinity_views.withdraw, name='withdraw'),'''

    path('pricing/', infinity_views.pricing, name='pricing'),
    path('blog/', infinity_views.blog, name='blog'),
    
    path('login/', infinity_views.signin, name='login'),
    path('logout/', infinity_views.signout, name='logout'),
    path('register/', infinity_views.register, name='register'),

    path('dashboard/', infinity_views.dashboard, name='dashboard'),
    path('contact/', infinity_views.contact, name='contact'),
    #path('send-email/', infinity_views.send_email, name='send-email'),
    path('thank-you/', infinity_views.thank_you, name='thank_you'),
  
  #  path('buy-airtime/', infinity_views.buy_airtime, name='buy_airtime'),

    # TRANSACTIONS
    # path('transactions/', include('transactions.urls')),

    path("redirect_from_dashboard/", infinity_views.get_function_chosen, name = "get_function_chosen"),
    path("account_management/", infinity_views.account_management, name='account_management'),
    path("process_account_action/", infinity_views.get_account_action, name='get_account_action'),
    path("withdraw/", infinity_views.withdraw, name='withdraw'),
    path("deposit/", infinity_views.deposit, name='deposit'),
    path("stat_gen/", infinity_views.stat_gen, name='stat_gen'),
    path("get_stat_gen/", infinity_views.get_transaction_action, name='get_transaction_action'),
    path("show_ecs_options/", infinity_views.show_ecs_options, name='show_ecs_options'),
    path("redirect_ecs/", infinity_views.redirect_ecs, name='redirect_ecs'),
    path("start_ecs/", infinity_views.start_ecs, name='start_ecs'),
    path("store_new_ecs_data/", infinity_views.store_new_ecs_data, name='store_new_ecs_data'),
    path("show_due_bills/", infinity_views.show_due_bills, name='show_due_bills'),
    path("pay_bill/", infinity_views.pay_bill, name='pay_bill'),
]


handler404 = 'InfinityFinance.views.error_404'  # Correct the handler404 to use the correct module path
