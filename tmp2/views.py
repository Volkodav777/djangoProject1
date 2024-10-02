from django.http import HttpResponse


# Create your views here.
def catalog_3 (request):
    return HttpResponse('Всёё мужики. Отбой.')

def catalog_4 (request):
    return HttpResponse('Да чё ты топчешься? Если есть что - выкладывай, нет - проваливай.')

def catalog_5 (request):
    return HttpResponse('Покедова!')