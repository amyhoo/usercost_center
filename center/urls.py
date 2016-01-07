"""billing_center URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,patterns
from django.views.generic import TemplateView
from center import bdetails,business,recost
from center import views
urlpatterns = patterns('',
   url(r'^index$', views.indexView.as_view(),),
   url(r'^bdetails/$', bdetails.BillDetailsView.as_view()),
   url(r'^recost$', recost.RecentCostView.as_view(),),
   url(r'^predirect', bdetails.pay_redirect,),
   url(r'^fcast$',bdetails.cost_forecast,),
   url(r'insRecharge', business.insteadRecharge,),
   url(r'gRecharge/(?P<account_id>.+)$', business.giftRecharge,),
   url(r'^busimanage$', business.BusinessView.as_view(),),
)
