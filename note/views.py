from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import User, Note
from django import forms
import datetime

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
        print(request.POST)
        isarchive = request.POST['archive'] == 'True'
        noteid = int(request.POST['noteid'])
        note = Note.objects.get(pk=noteid)
        note.isarchive = isarchive
        note.save()
        print(note.isarchive)
    notes = Note.objects.filter(isarchive=False).all()
    notes = notes.order_by("-timestamp").all()
    return render(request, 'note/allnote.html', {
        "notes": notes
    })

def archive(request):
    if request.method == "POST":
        print(request.POST)
        isarchive = request.POST['archive'] == 'True'
        noteid = int(request.POST['noteid'])
        note = Note.objects.get(pk=noteid)
        note.isarchive = isarchive
        note.save()
        print(note.isarchive)
    notes = Note.objects.filter(isarchive=True).all()
    notes = notes.order_by("-timestamp").all()
    return render(request, 'note/archive.html', {
        'notes': notes
    })
