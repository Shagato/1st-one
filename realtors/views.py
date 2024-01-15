from django.shortcuts import render
#from listings.models import listing
#from django.http import HttpResponse

def realtor(request):
    

    return render(request, 'realtors/realtors.html')
