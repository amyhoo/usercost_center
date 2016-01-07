from django.shortcuts import render
import django.views.generic as classview
from django.http import HttpResponse,HttpResponseRedirect
from views.base import BillReqMixin
from api.requestClient import request as billing_req
import json
class  BillDetailsView(BillReqMixin,classview.TemplateView):
    '''
    账户详情
    '''
    template_name= "billdetails/details_ajax.html"
    def get(self, request, *args, **kwargs):
        return super(BillDetailsView,self).get(request, *args, **kwargs)

    def get_data(self):
        account_id=self.request.session.get("account")["account_id"]
        account_info={}
        for key,value in billing_req("///"+account_id)["account"].items():
            if key =="" or key=="" or key=="":
                account_info[key]=string.atof(value)
        account_info[""]=account_info[""] if account_info[""]>0 else account_info[""]+account_info[""]
        account_info[""]=account_id
        title_list=[]
        return {"":account_info,'':account_info['']+account_info[''],"":title_list}

def pay_redirect(request):
    '''
    支付请求
    :param request:
    :return:
    '''
    from hashlib import md5
    import settings

    try:
        from urllib import urlencode
    except ImportError:
        from urllib.parse import urlencode
    MD5_KEY= settings.MD5_KEY

    def _generate_md5_sign(params):
        #md5加密生成签名
        src = '&'.join(['%s=%s' % (key, value) for key,value in sorted(params.items())]) + MD5_KEY
        return md5(src.encode('utf-8')).hexdigest()

    def _generate_payment_url(params_signed):
        return '%s?%s' % (settings.PAYMENT_URL, urlencode(params_signed))

    account_id=request.GET.get("")
    agented_id=request.GET.get("")

    if agented_id:
        params={"":account_id,"":agented_id}
    else:
        params={"":account_id}

    sign=_generate_md5_sign(params)
    params.update({"":sign})
    payment_url=_generate_payment_url(params)
    return HttpResponseRedirect(payment_url)

def cost_forecast(request):
    account_id=request.session.get("")[""]
    #account_id="5689sfshfhsdhiojfdsjofi"
    return_list=billing_req("///"+account_id)[""]
    return HttpResponse(json.dumps(return_list))