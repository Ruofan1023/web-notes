# Capstone: Note

This is a project for CS50’s Web Programming with Python and JavaScript. This is a web note-taking app that allows users to create quick notes to record down their thoughts.

## Features

### Create A New Note
A user can create a new note including the title as well as the content. A timestamp will also be given to the note on its created time.

### View All Notes
A user can view all of the notes created

### Archive Notes
A user can archive a note that is no longer needed. The option to unarchive the note is also provided.

### Delete A Note
A note can be permalently deleted under any state, whether it is in the archive or not.

### Pin A Note 
Pin any note to the top of the screen for quicker access and convenience. The lastest pinned note will always stay on top in a stack manner. Any pinned notes can also be unpinned.

### Lock and Unlock a note
Notes with sensitive information can be locked with one click. The user must enter his/her account passsword in order to unlock the note to see the content.

### Search for notes
Search all notes that contains some specific words in either their title or their content. The results will be displayed as a list of notes.

## Distinctiveness and Complexity
This Note app contains many features that are distinctive from all the projects in this course. Specifically, features such as deleting,pinning and locking notes have never occurred in my previous projects, making this note-taking app unique. I also put in lots of thinking and effort in coming up with the ideas as well as the actual design and implementation. For example, I tried to simulate a somewhat last-in-first-out-like data structure for the pinned note feature where a newly pinned note will always stay at the top of the pinned list. This data structure also ensures that removing any pinned note will not change the relative order of other pinned notes. Therefore, I believe my project satisfies the distinctiveness requirement.

This app is also a complex one. The most difficult part in creating this app will be coordinating and managing a note's state. A note object in this app has the highest number of states compared to all the objects in previous projects, making the proper management of a note quite challenging.  Since a note can be pinned/unpinned, archived/unarchived and locked/unlocked, and must be arranged by their timestamps, a complex combination of different states give rise to the need to tackle many different situations in my implementation. Therefore, I believe my project satisfies the complexity requirement.

## Files
Here is a list of files that I have created and their content, excluding configuration files in ./capstone:

### ./manage.py
The entry point of the app.

### ./db.sqlite3
The database.

### ./note/views.py
Here are the functions that render a specific page with the required logic given a specific path.

### ./note/urls.py
Here is where the routing of the app is specified.

### ./note/models.py
Here is where the object models used in database are created.

### ./note/apps.py
Some configuration of the app.

### ./note/__init__.py
The __init__.py files are required to make Python treat directories containing the file as packages.

### ./note/templates/note/allnote.html
The view for a list of all notes.

### ./note/templates/note/archive.html
The view for a list of archived notes.

### ./note/templates/note/index.html
The page for creating a new note.

### ./note/templates/note/layout.html
The page that determines the layout for all other page views.

### ./note/templates/note/login.html
The login interface.

### ./note/templates/note/noteform.html
A single form that let user create and submit a note

### ./note/templates/note/register.html
The page for a new user to register for the app.

### ./note/templates/note/search.html
The page for user to search for notes

### ./note/static/note/node.js
The javscript logic for the app's lock and unlock feature.

### ./note/migrations/
All files here are gradual migrations after the django models are modified.

## Run the application
1. Download the source code in this github repository.
2. In your terminal, `cd` into the root directory of the project (`capstone`).
3. Run `python manage.py makemigrations note` to make migrations for the note app.
4. Run `python manage.py migrate` to apply migrations to your database.
5. Run `python manage.py runserver` to start up the Django web server, and visit the website in your browser.

