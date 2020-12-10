# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

@login_required(login_url="/login/")
def index(request):

    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


from django.db import connection
import pandas as pd
@login_required(login_url="/login/")
def tests(request):
    sql = """select tendonvi_gdv, ten_ctv, FIBER_200_0,FIBER_200_3,FIBER_200_7,FIBER_200_15
            from db_nha.reports.BRCD_PTM_TH
            where thang='202011'
            	and NVVNPT=1
            order by tendonvi_gdv"""
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    field_names = cursor.description

    pbh = [col[0] for col in results]
    pbh = list(set(pbh)) #lọc trung phong ban hang

    html_template = loader.get_template( 'tests.html' )
    context = {
        'field_names': field_names,
        'results': results,
        'pbh': pbh
    }
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def new_page(request):

    html_template = loader.get_template( 'new_page.html' )
    context = {
    }
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def dashboard_detail(request, slug):
    post = Dashboard.objects.get(slug=slug)
    html_template = loader.get_template( 'dashboard_detail.html' )
    return render(request, 'dashboard_detail.html', {'dashboard': dashboard})
