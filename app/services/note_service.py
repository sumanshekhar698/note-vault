from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Note, User
from app.schemas import NoteCreate, NoteUpdate


def get_owned_note(db: Session, user: User, note_id: int) -> Note:
    note = db.get(Note, note_id)
    if note is None or note.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note


def list_notes(db: Session, user: User) -> list[Note]:
    stmt = (
        select(Note)
        .where(Note.user_id == user.id)
        .order_by(Note.is_pinned.desc(), Note.updated_at.desc())
    )
    return list(db.scalars(stmt))


def create_note(db: Session, user: User, payload: NoteCreate) -> Note:
    note = Note(**payload.model_dump(), user_id=user.id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def update_note(db: Session, user: User, note_id: int, payload: NoteUpdate) -> Note:
    note = get_owned_note(db, user, note_id)
    changes = payload.model_dump(exclude_unset=True, exclude_none=True)
    for field, value in changes.items():
        setattr(note, field, value)
    db.commit()
    db.refresh(note)
    return note


def delete_note(db: Session, user: User, note_id: int) -> None:
    note = get_owned_note(db, user, note_id)
    db.delete(note)
    db.commit()