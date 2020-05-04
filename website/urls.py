"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from portfolio.views import PortfolioList, PortfolioDetail, AboutPage, ContactPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PortfolioList.as_view(), name='portfolio_list'),
    path('project/<int:pk>', PortfolioDetail.as_view(), name='portfolio_detail'),
    path('about/', AboutPage.as_view(), name='about'),
    path('contact', PortfolioList.as_view(), name='contact'),
]
