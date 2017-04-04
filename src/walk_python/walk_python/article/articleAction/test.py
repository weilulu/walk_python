# -*- coding: UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def test(request):
    print 'hello-------------'
    now = datetime.datetime.now()
    return render_to_response('test/test.html',{'test':now})
