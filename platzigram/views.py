# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    # Return a JSON response with sorted integers
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        "status": "ok",
        "numbers": sorted_ints,
        "message": "integers sorted successfully"
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json")


def say_hi(request, name, age):
    #Return a greeting
    if age < 12:
        message = "Sorry, {}  you are not allowed here, your age is {}".format(name,age)
        
    else:
        message = "Hello, {} Welcome to PlatziGram , your age is {} ".format(name,age)
    
    return HttpResponse(message)