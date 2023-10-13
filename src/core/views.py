from rest_framework.decorators import api_view
from rest_framework import status
from core.configurations.configurationhandler import (
    EXCEPTIONS 
)
from rest_framework.response import Response
from django.shortcuts import render

from core.exceptions.exceptionshandler import NotFound

@api_view(['GET', 'POST'])
def error404(request, exception):
    """
    handler for 404 error
    """
    raise NotFound("The requested resource was not found")

@api_view(['GET', 'POST'])
def error500(request):
    """
    handler for 500 error
    """
    return Response(
        EXCEPTIONS['INTERNAL_SERVER_ERROR'], 
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )

@api_view(['GET'])
def ping(req):
    """
    check if service is active.
    Only GET Allowed. Other Methods will show 405
    """
    return Response(
        {"success" : True, "result" : "Service is Active" }, 
        status=status.HTTP_200_OK
    )

def index(request):
    return render(request, 'core/index.html')