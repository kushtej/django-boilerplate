from rest_framework.views import exception_handler
from rest_framework.exceptions import *
from rest_framework.response import Response
from rest_framework import status

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

def custom_exception_handler(exc, context):
    default_response = exception_handler(exc, context)
    return Response({
        'success' : False,
        'error' : {
            'message': default_response.data['detail'],
            'code':    default_response.data['detail'].code.upper()
        }
    },status=default_response.status_code)