from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from inPage.models import notes
from api.serializer import noteSeralizer

@api_view(['GET'])
def getNotes(request): # this function passes all the notes
    if request.method=="GET":
        allNotes=notes.objects.all()
        serializedModel=noteSeralizer(allNotes,many=True)
        return Response(serializedModel.data)


@api_view(['GET']) # this function passes only one note
def getOneNote(request,serial):
    if request.method=="GET":
        oneNote=notes.objects.get(serial=serial)
        serializedModel=noteSeralizer(oneNote, many=False)
        return Response(serializedModel.data)

@api_view(['POST']) #this function creates a note in the database
def addNotes(request):
    if request.method=="POST":
        newNote=noteSeralizer(data=request.data)
        if newNote.is_valid():
            newNote.save()
            return Response(newNote.data)
        return Response(newNote.errors)

@api_view(['PUT','PATCH'])
def updateNote(request,serial):        
    if request.method=="PUT":
        oldNote=notes.objects.get(serial=serial)
        updatedNote = noteSeralizer(instance=oldNote , data=request.data)
        if updatedNote.is_valid():
            updatedNote.save()
            return Response(updatedNote.data)
        return Response(updatedNote.errors)

    else:
        oldNote=notes.objects.get(serial=serial)
        updatedNote = noteSeralizer(instance=oldNote , data=request.data, partial=True)
        if updatedNote.is_valid():
            updatedNote.save()
            return Response(updatedNote.data)
        return Response(updatedNote.errors)


@api_view(['DELETE'])
def deleteNote(request,serial):
    if request.method=="DELETE":
        # oldNoteID=request.data['serial'] #can use oldNoteID to use the json data
        
        try:
            oldNote=notes.objects.get(serial=serial)#this approach is to use the url hitting method only
            oldNote.delete()
            return Response({'message':'Note has been deleted from database'})
        except :
            return Response({'message':'No object with this ID exists'})
