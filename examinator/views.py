from __future__ import unicode_literals, absolute_import
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt

def health_check(request):
    return HttpResponse("OK", status=200)
