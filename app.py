from models import Artwork, Artist
from peewee import SqliteDatabase
db = SqliteDatabase('art.sqlite')

def main():
    db.create_tables([Artist, Artwork])


if __name__ == "__main__":
    main()
