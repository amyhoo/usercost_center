# -*- coding: utf-8 -*-
#######################################################################################
# 处理session过期
#######################################################################################
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import datetime
class Session_Timeout(object):
    def process_request(self, request):
        if request.is_ajax():
            if not request.session.get("account"):#request.session.get_expiry_date().replace(tzinfo=None)<datetime.datetime.today()
                return HttpResponse("_session_time_out")
        else:
            return HttpResponseRedirect("login")

