from django.shortcuts import render
from pathlib import Path
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    p = Path('.').glob('*.mp3')
    files = {}
    for mfile in p:
        files[mfile.name] = mfile.as_posix()
    template = loader.get_template('Item_Center/index.html')
    context = {
        'files':files,
    }
    return HttpResponse(template.render(context,request))

