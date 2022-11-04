from .models import Logg


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin/'):
            log = Logg.objects.create(path=request.path, method=request.method)
            if request.method == 'POST':
                log.data = request.POST
                log.save()
        response = self.get_response(request)
        return response
