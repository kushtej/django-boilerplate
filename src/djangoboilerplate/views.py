from rest_framework.decorators import api_view
from core.exceptions.exceptionshandler import NotFound, APIException


@api_view(["GET", "POST"])
def error404(request, exception):
    """
    handler for 404 error
    """
    raise NotFound("The requested resource was not found")


@api_view(["GET", "POST"])
def error500(request):
    """
    handler for 500 error
    """
    raise APIException("A server error occurred. Please contact Administrator")
