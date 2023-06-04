from rest_framework.views import exception_handler
from rest_framework.exceptions import *
from rest_framework.response import Response
from rest_framework import status

import json

from core.configurations.configurationhandler import EXCEPTIONS


class ServiceUnavailable(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "the server is currently unable to handle the request"
    default_code = 'SERVICE_UNAVAILABLE'

class PreconditionFailed(APIException):
    status_code = status.HTTP_412_PRECONDITION_FAILED
    default_detail = "Mandetory Resource for this operation missing."
    default_code = 'PRECONDITION_FAILED'

class UnsupportedMediaType(APIException):
    status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    default_detail = "Mediatype not supported."
    default_code = 'UNSUPPORTED_MEDIA_TYPE'

class Conflict(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Duplicate Record found for this operation"
    default_code = 'CONFLICT'

def VTAnalyser_exception_handler(exc, context):

    if isinstance(exc, ParseError):
        return Response(EXCEPTIONS['BAD_REQUEST'], status=400)

    if isinstance(exc, NotAuthenticated):
        return Response(EXCEPTIONS['NOT_AUTHENTICATED'], status=401)

    elif isinstance(exc, AuthenticationFailed):
        return Response(EXCEPTIONS['AUTHENTICATION_FAILED'], status=403)
    
    elif isinstance(exc, PermissionDenied):
        return Response(EXCEPTIONS['INVALID_GROUP'], status=403)
    
    elif isinstance(exc, NotFound):
        return Response(EXCEPTIONS['NOT_FOUND'], status=404)

    elif isinstance(exc, Conflict):
        return Response(EXCEPTIONS['CONFLICT'], status=409)

    elif isinstance(exc, UnsupportedMediaType):
        return Response(EXCEPTIONS['UNSUPPORTED_MEDIA_TYPE'], status=415)
    
    elif isinstance(exc, ServiceUnavailable):
        return Response(EXCEPTIONS['SERVICE_UNAVAILABLE'], status=503)

    elif isinstance(exc, PreconditionFailed):
        return Response(EXCEPTIONS['PRECONDITION_FAILED'], status=412)
    
    elif isinstance(exc, APIException):
        return Response(EXCEPTIONS['INTERNAL_SERVER_ERROR'], status=500)

    return exception_handler(exc, context)