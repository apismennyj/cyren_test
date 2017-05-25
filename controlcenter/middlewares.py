from controlcenter.models import User, get_or_none


#Since we're not using Djano Auth - we need to set up cookie to sign/verify user
class CustomAuthenticationMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.current_user = get_or_none(User, pk=request.COOKIES.get('session_id'))
        response = self.get_response(request)

        return response
