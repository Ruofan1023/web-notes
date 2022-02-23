from xml.etree.ElementTree import PI
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import User, Note, PinQueue
from django import forms
import datetime
import json
from json import JSONEncoder
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, "note/index.html", {
        'form': NoteForm()
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "note/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "note/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "note/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "note/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "note/register.html")

class NoteForm(forms.Form):
    title = forms.CharField(max_length=160)
    content = forms.CharField(widget=forms.Textarea)

def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST);
        if form.is_valid():
            data = form.cleaned_data
            title = data['title']
            content = data['content']
            print(f'title: {title}')
            print(f'content: {content}')
            note = Note(user=request.user, title=title, content=content)
            note.save()
    return redirect('index')

def allnote(request):
    
    if request.method == "POST":
        print(request)
        if (request.POST['type'] == 'archive'):
            isarchive = request.POST['archive'] == 'True'
            noteid = int(request.POST['noteid'])
            note = Note.objects.get(pk=noteid)
            note.isarchive = isarchive
            note.save()
        if (request.POST['type'] == 'pin'):
            noteid = int(request.POST['noteid'])
            print(f'pin {noteid}')
            pin_queue = None
            if (not PinQueue.objects.exists()):
                pin_queue = PinQueue.objects.create()
            else:
                pin_queue = PinQueue.objects.first()
            queue = pin_queue.queue
            queue.insert(0, noteid)
            print(queue)
            pin_queue.save()
        if (request.POST['type'] == 'unpin'):
            noteid = int(request.POST['noteid'])
            pin_queue = PinQueue.objects.first()
            queue = pin_queue.queue
            queue.remove(noteid)
            print(queue)
            pin_queue.save()
        if (request.POST['type'] == 'delete'):
            noteid = int(request.POST['noteid'])
            toDelete = Note.objects.get(pk=noteid)
            try:   
                PinQueue.objects.first().queue.remove(toDelete.id)
            except ValueError:
                pass
            toDelete.delete()

    notes = Note.objects.filter(isarchive=False).all()
    ordered_notes = notes.order_by("-timestamp").all()
    unpinned_notes = filter(lambda note: note.id not in PinQueue.objects.first().queue, ordered_notes)
    # pinned_notes = filter(lambda note: note.id in PinQueue.objects.first().queue, notes)

    def getPinned(noteid):
        try:
            note = Note.objects.get(pk=int(noteid))
        except ObjectDoesNotExist:
            return None
        if (not note.isarchive):
            return note
        return None
    pinned_notes = map(getPinned, PinQueue.objects.first().queue)
    pinned_notes = list(filter(lambda note: note != None, pinned_notes))
    return render(request, 'note/allnote.html', {
        "notes": unpinned_notes,
        "pinned_notes": pinned_notes
    })

def archive(request):
    if request.method == "POST":
        print(request.POST)
        if (request.POST['type'] == 'archive'):
            isarchive = request.POST['archive'] == 'True'
            noteid = int(request.POST['noteid'])
            note = Note.objects.get(pk=noteid)
            note.isarchive = isarchive
            note.save()
        if (request.POST['type'] == 'delete'):
            noteid = int(request.POST['noteid'])
            toDelete = Note.objects.get(pk=noteid)
            try:
                PinQueue.objects.first().queue.remove(toDelete.id)
            except ValueError:
                pass
            toDelete.delete()
    notes = Note.objects.filter(isarchive=True).all()
    notes = notes.order_by("-timestamp").all()
    return render(request, 'note/archive.html', {
        'notes': notes
    })
