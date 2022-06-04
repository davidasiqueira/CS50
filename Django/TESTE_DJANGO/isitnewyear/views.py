from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def isitnewyear(request):
    
    now = datetime.datetime.now()
    
    return render(request, 'isitnewyear/isitnewyear.html', {
        "isitnewyear": now.month == 1 and now.day == 1
    })
