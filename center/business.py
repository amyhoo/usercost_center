# -*- coding: utf-8 -*-
from django.shortcuts import render
import django.views.generic as classview
from django.http import HttpResponse,HttpResponseRedirect
from views.base import BillReqMixin,HomePageView
from api.requestClient import request as billing_req

class  BusinessView(BillReqMixin,HomePageView):
    '''
    子帐号账户管理
    '''
    template_name= "business/instead_recharge.html"
    def get(self, request, *args, **kwargs):
        return super(BusinessView,self).get(request, *args, **kwargs)

    def get_data(self):
        return_info={}
        pass
        return return_info


def  insteadRecharge(request):
    '''
    近期消费记录
    '''
    recharge_data=json.loads(request.POST["recharge"])
    request_url=""
    response=billing_req(request_url,data=json.dumps(recharge_data),method="POST")
    if response['success']=="success":
        return_data="success"
    else:
        return_data="fail"
    return HttpResponse(return_data)

def  giftRecharge(request,*args,**kwargs):
    '''
    近期消费记录
    '''
    account_id=kwargs["account_id"]
    recharge_data=json.loads(request.POST["recharge"])
    request_url=""+account_id
    response=billing_req(request_url,data=json.dumps(recharge_data),method="POST")
    if response['success']=="success":
        return_data="success"
    else:
        return_data="fail"
    return HttpResponse(return_data)