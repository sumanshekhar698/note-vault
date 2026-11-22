from sqlalchemy import Column, ForeignKey, Table

from app.database import Base

# This is a Python variable that stores the SQLAlchemy Table object.
# Table() is a SQLAlchemy function used to define a database table directly.
note_tags = Table(
    "note_tags",
    Base.metadata,
    Column("note_id", ForeignKey("notes.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)