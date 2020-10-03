from models import Artist, Artwork
from unittest import TestCase
from peewee import SqliteDatabase, IntegrityError


MEMORY = True
db = ":memory:" if MEMORY else "test.db.sqlite"

# test setup from peewee
# http://docs.peewee-orm.com/en/latest/peewee/database.html?highlight=testing#testing-peewee-applications
MODELS = [Artist, Artwork]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(db)


class TestArtist(TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

        # If we wanted, we could re-bind the models to their original
        # database here. But for tests this is probably not necessary.

    def test_artist_created(self):
        name = 'artist name'
        email = 'artist@emails.com'
        artist = Artist.create(name=name, email=email)
        self.assertTrue(artist.name == name)
        self.assertTrue(artist.email == email)

    def test_artist_unique_name_constraints(self):
        name = 'artist name'
        email = 'artist@emails.com'
        Artist.create(name=name, email=email)
        with self.assertRaises(IntegrityError):
            Artist.create(name=name, email='email@example.com')

    def test_artist_unique_email_constraints(self):
        name = 'artist name'
        email = 'artist@emails.com'
        Artist.create(name=name, email=email)
        with self.assertRaises(IntegrityError):
            Artist.create(name='new name', email=email)

    def test_artist_empty_name_constraints(self):
        email = 'artist@emails.com'
        with self.assertRaises(IntegrityError):
            Artist.create(email=email)

    def test_artist_empty_email_constraints(self):
        name = 'artist name'
        with self.assertRaises(IntegrityError):
            Artist.create(name=name)


class TestArtwork(TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)
        self.artist = Artist.create(name='sample artist', email='example@example.com')

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables(MODELS)

        # Close connection to db.
        test_db.close()

    def test_artwork_created(self):
        name = "painting"
        price = 100
        artwork = Artwork.create(artist=self.artist, name=name, price=price, sold=False)
        self.assertTrue(artwork.name == "painting")

    def test_artwork_repects_unique_name(self):
        name = "painting"
        price = 100
        Artwork.create(artist=self.artist, name=name, price=price, sold=False)
        with self.assertRaises(IntegrityError):
          Artwork.create(artist=self.artist, name=name, price=price, sold=False)

    def test_artwork_repects_foreign_key_constraint(self):
        name = "painting"
        price = 100
        with self.assertRaises(IntegrityError):
          Artwork.create(name=name, price=price, sold=False)

    def test_artwork_can_be_retrieved_by_user(self):
        name = "paintings"
        price = 100.24
        Artwork.create(artist=self.artist, name=name, price=price, sold=False)
        Artwork.create(artist=self.artist, name=f"{name}1", price=price, sold=False)
        Artwork.create(artist=self.artist, name=f"{name}2", price=price, sold=False)
        self.assertEqual(len(self.artist.artworks), 3)
