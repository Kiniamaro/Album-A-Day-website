from django.shortcuts import render
from django.http import HttpResponse

from albumADay.models import Album

def index(request):
    
    album_list = Album.objects.order_by('pub_date')
    context = {'album_list': album_list}
    return render(request, 'albumADay/index.html', context)
    
def detail(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {'album': album}
    return render(request, 'albumADay/detail.html', context)

