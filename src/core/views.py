from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.response import Response
from django.shortcuts import render


@api_view(["GET"])
def ping(req):
    """
    check if service is active.
    Only GET Allowed. Other Methods will show 405
    """
    return Response({"success": True, "result": "Service is Active"}, status=status.HTTP_200_OK)


def index(request):
    return render(request, "core/index.html")
