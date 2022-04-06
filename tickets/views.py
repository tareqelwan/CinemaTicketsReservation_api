from django.http import JsonResponse
from django.shortcuts import render
from tickets.models import Guest,Movie,Reservation

# (1) without rest and no model - Function Based View : FBV
def no_rest_no_model(request):
    
    guests = [
        {
            'id':1,
            'name': 'Omar',
            'mobile':111111,
        },
        {
            'id':2,
            'name': 'Ahmed',
            'mobile':222222,
        },
        {
            'id':3,
            'name': 'Hassan',
            'mobile':333333,
        },

    ]

    return JsonResponse(guests,safe=False) # safe=False because >>> data not hashed

# (2) no_rest_from_model
def no_rest_from_model(request):
    data = Guest.objects.all()
    response={
        'guests':list(data.values('name','mobile')),
    }
    return JsonResponse(response)

