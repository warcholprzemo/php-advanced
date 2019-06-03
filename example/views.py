from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from example.forms import GiftListForm
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


class GiftListCreateView(CreateView):
    model = GiftList
    form_class = GiftListForm
    success_url = '/gift_list/add/'
    template_name = 'example/add.html'


class GiftListUpdateView(UpdateView):
    model = GiftList
    form_class = GiftListForm
    template_name = 'example/add.html'

    def get_success_url(self):
        return reverse('list_gfl')

