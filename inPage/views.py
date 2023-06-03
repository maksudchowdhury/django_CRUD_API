from django.shortcuts import render
from django.http import HttpResponse
from inPage.models import notes
# Create your views here.
def index(request):
    return render(request,'inPageIndex.html')
def saveNote(request):
    if request.method=='POST':
        title=request.POST['noteTitle']
        note=request.POST['noteDescription']
        newNote=notes.objects.create(title=title,desc=note)
        notes.save(newNote)
        return index(request)