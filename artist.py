from models import Artist
from peewee import SqliteDatabase, IntegrityError
import ui

def get_name_and_email():
  name = ui.get_string('Enter artist name: ')
  email = ui.get_string('Enter artist email: ')
  return name, email

def create():
  try:
    name, email = get_name_and_email()
    artist = Artist.create(name=name, email= email)
    ui.display('Success')
    ui.display(f"ID: {artist.id}\nName: {artist.name}\nEmail: {artist.email}")

  except IntegrityError:
    ui.display('Artist already exists')

def show_all():
    artists = Artist.select()
    for artist in artists:
        ui.display(f"ID: {artist.id}\nName: {artist.name}\nEmail: {artist.email}")

def get_by_id():
    id = ui.get_positive_integer("Enter artist id: ")
    artist = Artist.get(Artist.id == id)
    ui.display(f"ID: {artist.id}\nName: {artist.name}\nEmail: {artist.email}")
    return artist

def update_by_id():
    show_all()
    artist = get_by_id()
    name, email = get_name_and_email()
    artist.name = name
    artist.email = email
    artist.save()
    ui.display("Success")
    ui.display(f"ID: {artist.id}\nName: {artist.name}\nEmail: {artist.email}")
