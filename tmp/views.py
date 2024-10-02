from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Привет, Джанга')

def catalog (request):
    return HttpResponse('проходи не задерживайся')

def catalog_2 (request):
    return HttpResponse('не шелести особо')


