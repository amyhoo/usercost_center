# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from billing_center.api.requestClient import request as req
from billing_center.api.requestClient import getAccount
from billing_center.views.base import HomePageView
import json
from django.conf import settings
from billing_center.center.utils import getMD5

class indexView(HomePageView):
    template_name = "base.html"

    def get(self, request, *args, **kwargs):
        if request.session.get('account',default=None) is None:
            return HttpResponseRedirect(settings.HORIZON_URL+'/auth/logout')
        return super(indexView, self).get(request, *args, **kwargs)

    def get_data(self):
        account_id=self.request.GET['account_id']
        m=None
        if self.request.GET.has_key('m'):
            m=self.request.GET['m']
        if 'sign' in self.request.GET:
            sign=self.request.GET['sign']
            md5_key=settings.MD5_KEY
            if self.request.session.has_key('account'):
                if self.request.session.get('account')['account_id']!=account_id:
                    self.request.session['account']=None
            if getMD5(account_id+md5_key) !=sign:
                return
        return {'username': self.request.session['account']['username'],'horizon_url':settings.HORIZON_URL,'m':m}
