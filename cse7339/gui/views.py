from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def index(request):
    template = loader.get_template('index.html')
    return render(request, 'index.html')

def upload_file(request):
    uploaded = False
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        file_name = myfile.name #fs.save(myfile.name, myfile)
        uploaded = True
        context = {'file_name': file_name,
                   'uploaded': uploaded}
        return render(request, 'upload.html', context)
    return render(request, 'upload.html')
