from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

from albumADay.models import Album

def index(request):
    
    album_list = Album.objects.order_by('pub_date')
    context = {'album_list': album_list}
    return render(request, 'albumADay/index.html', context)
    
def detail(request, album_id):
    album = Album.objects.get(id=album_id)
    year_2015 = 1420070400
    day_of_id = int(album_id) * 86400 # number of seconds in a day
    d = date.fromtimestamp(day_of_id + year_2015)
    context = {'album': album, 'date': d.strftime("%A, %B %d")}
    return render(request, 'albumADay/detail.html', context)

