"""
Views for reporting stock counts/actuals and resetting
"""

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import pluralize
from django.urls import reverse
from django.utils.safestring import mark_safe

from django.http import HttpResponse

from core.models import LocationStockCount, LocationStockReport, Location

@staff_member_required()
def stock_landing_page(request):
    return render(request,'reporting/stock_landing_page.html')

@staff_member_required()
def stock_report(request, stock_action):
    print(stock_action)
    if request.method == 'POST':
        location = Location.objects.get(pk=request.POST.get('location'))
        actual_count = request.POST.get('actual_count')
        stock_count = request.POST.get('stock_count')
        #create a stock report and a stock count for the location
        location.stock_reports.create(actual_amount=actual_count)
        location.stock_counts.create(count=stock_count)
        messages.success(request,"Successfully stocked and submitted a report for {}".format(location))

    if stock_action == 'restock':
        locations = Location.objects.checkout().filter(admin_location=False)
    else:
        locations = Location.objects.checkin().filter(admin_location=False)
    return render(request,'reporting/stock.html',{
        "locations": locations,
        "stock_action": stock_action,
    })
