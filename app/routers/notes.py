from fastapi import APIRouter, status

from app.core.deps import CurrentUser
from app.database import SessionDep
from app.schemas import NoteCreate, NoteRead, NoteUpdate
from app.services import note_service

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("", response_model=list[NoteRead])
def list_notes(db: SessionDep, user: CurrentUser):
    return note_service.list_notes(db, user)


@router.post("", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, db: SessionDep, user: CurrentUser):
    return note_service.create_note(db, user, payload)


@router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: int, db: SessionDep, user: CurrentUser):
    return note_service.get_owned_note(db, user, note_id)


@router.patch("/{note_id}", response_model=NoteRead)
def update_note(note_id: int, payload: NoteUpdate, db: SessionDep, user: CurrentUser):
    return note_service.update_note(db, user, note_id, payload)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: SessionDep, user: CurrentUser) -> None:
    note_service.delete_note(db, user, note_id)