from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from example.models import GiftList


#def hello_world(request):
#    return HttpResponse('Hello World!')

def hello_world(request):
    return render(request, 'example/index.html', {})


def hello_name(request, name):
    return HttpResponse(f'Hello {name}')


def simple_list_view(request):
    gfl_entries = GiftList.objects.all()
    return render(
        request,
        'example/list.html',
        {'gfl_entries': gfl_entries},
    )


class GiftListView(ListView):
    model = GiftList
    template_name = 'example/list.html'
    context_object_name = 'gfl_entries'
