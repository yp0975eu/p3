from models import Artwork, Artist
from peewee import SqliteDatabase, IntegrityError
import artist
import artwork
import ui
from menu import Menu

db = SqliteDatabase('art.sqlite')

def build_menu():
    menu = Menu()
    menu.add("1", 'Add an Artist', artist.create)
    menu.add("2", 'View all Artists', artist.show_all)
    menu.add("3", 'Show Artists by ID', artist.get_by_id)
    menu.add("4", 'Update Artists by ID', artist.update_by_id)
    menu.add("6", 'Add Artwork', artwork.create)
    menu.add("7", 'Show All Arwork',  artwork.show_all)
    menu.add("8", 'Show Artwork by Id', artwork.get_by_id)
    menu.add("9", 'Update Artwork  by ID', artwork.update_by_id)
    menu.add("10", 'Show all available Artwork', artwork.show_all_available)
    menu.add("11", 'Show all sold Artwork', artwork.show_all_sold)
    menu.add("12", 'Show all available Artwork by artist', artwork.show_all_available_by_artist)
    menu.add("13", 'Show all sold Artwork by artist', artwork.show_all_sold_by_artist)
    menu.add("q", 'quit', lambda: exit())
    return menu

def main():
    db.create_tables([Artist, Artwork])
    menu = build_menu()
    while True:
      menu.show()
      user_input = input('\nenter a menu option: ')
      option = menu.get(user_input)
      if option:
        option()


if __name__ == "__main__":
    main()
