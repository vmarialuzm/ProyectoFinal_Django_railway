from ipware import get_client_ip
from .models import IPAddress


def is_valid_ip(get_response):
    def middleware(request):
        ip, is_routable = get_client_ip(request)
        response = get_response(request)
        IPAddress.objects.create(ip_address=ip)

        return response
    return middleware