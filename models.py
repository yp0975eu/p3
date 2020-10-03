from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, IntegerField, BooleanField
db = SqliteDatabase('art.sqlite')

"""
database table name is the same as the class name
"""


class Artist(Model):
    name = CharField(unique=True, null=False)
    email = CharField(unique=True, null=False)

    class Meta:
        database = db


class Artwork(Model):
    artist = ForeignKeyField(Artist, backref='artworks')
    name = CharField(unique=True, null=False)
    price = IntegerField(null=False, default=0)
    sold = BooleanField(null=False)

    class Meta:
        database = db
