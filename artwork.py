from models import Artwork
import artist as artist_control
from peewee import IntegrityError
import ui


def get_artwork_name():
    return ui.get_string('Enter artwork name: ')


def get_artwork_price():
    return ui.get_string('Enter price: ')


def get_artwork_sold_status():
    answer = ui.get_string_from_options(
        'Has this artwork been sold? Y or N? ', ['y', 'n'])
    return answer == 'y'


def create():
    try:
        artist_control.show_all()
        artist = artist_control.get_by_id()
        name = get_artwork_name()
        price = get_artwork_price()
        sold = False
        artwork = Artwork.create(
            artist=artist, name=name, price=price, sold=sold)
        ui.display('Success')
        ui.display(format_artwork(artwork))

    except IntegrityError:
        ui.display('Artwork already exists')


def show_all_sold():
    artworks = Artwork.select().where(Artwork.sold == True)
    if artworks:
        for artwork in artworks:
            ui.display(format_artwork(artwork))
    else:
        ui.display('No artwork found')


def show_all_available():
    artworks = Artwork.select().where(Artwork.sold == False)
    if artworks:
        for artwork in artworks:
            ui.display(format_artwork(artwork))
    else:
        ui.display('No artwork found')


def show_all_sold_by_artist():
    artist_control.show_all()
    artist = artist_control.get_by_id()
    artworks = Artwork.select().where(Artwork.sold == True, Artwork.artist == artist)
    if artworks:
        for artwork in artworks:
            ui.display(format_artwork(artwork))
    else:
        ui.display('No artwork found')


def show_all_available_by_artist():
    artist_control.show_all()
    artist = artist_control.get_by_id()
    artworks = Artwork.select().where(Artwork.sold == False, Artwork.artist == artist)
    if artworks:
        for artwork in artworks:
            ui.display(format_artwork(artwork))
    else:
        ui.display('No artwork found')


def show_all():
    artworks = Artwork.select()
    for artwork in artworks:
        ui.display(format_artwork(artwork))


def get_by_id():
    id = ui.get_positive_integer("Enter artwork by id: ")
    try:
        artwork = Artwork.get(Artwork.id == id)
        ui.display(format_artwork(artwork))
        return artwork
    except Exception as e:
        ui.display("Artwork does not exist")


def update_by_id():
    show_all()
    artwork = get_by_id()
    artwork.name = get_artwork_name()
    artwork.price = get_artwork_price()
    artwork.sold = get_artwork_sold_status()
    artwork.save()
    ui.display("Success")
    ui.display(format_artwork(artwork))


def delete():
    show_all()
    artwork = get_by_id()
    artwork.delete_instance()


def format_artwork(artwork):
    return f"ID: {artwork.id}\nArtist Name: {artwork.artist.name}\nArtwork Name: {artwork.name}\nPrice: {artwork.price}\nSold: {artwork.sold}"
