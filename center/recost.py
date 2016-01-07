from django.shortcuts import render
import django.views.generic as classview
from django.http import HttpResponse,HttpResponseRedirect
from views.base import BillReqMixin,HomePageView
from api.requestClient import request as billing_req
import json
from.utils import *
class  RecentCostView(BillReqMixin,classview.TemplateView):
    '''
    近期消费记录
    '''

    template_name= "recentcost/recentcost_ajax.html"
    def get(self, request, *args, **kwargs):
        return super(RecentCostView,self).get(request, *args, **kwargs)
    def get_data(self):
        resource_type_list=(
        )
        account_id=self.request.session.get("")[""]
        #account_id="5689sfshfhsdhiojfdsjofi"
        title_list=[{"":"","url":"//"}]
        request_url=""
        return_info=billing_req(request_url+account_id)["xxx"]
        return_info[""]=title_list
        return_info[""]=billing_req("...")["xxx"]
        return_info[""]=resource_type_list
        return return_info

def consumption_data(request):
    account_id=request.session.get("")[""]
    pageSize=int(request.GET[''])
    pageNo=int((float(request.GET[''])+1)/float(request.GET[''])+1)
    product_type=request.GET['']
    region=request.GET['']
    period=request.GET['']
    request_url=""
    result = billing_req(request_url)['']
    return_data={}
    return_data["rows"]=result.pop('consumptions')
    return_data["total"]=result.pop('total')
    return HttpResponse(json.dumps(return_data))