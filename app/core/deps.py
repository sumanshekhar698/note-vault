from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy import select

from app.database import SessionDep
from app.models import User

DEV_USER_EMAIL = "dev@notevault.local"


def get_current_user(db: SessionDep) -> User:
    """TEMPORARY: always returns the dev user. Replaced by JWT auth in Step 6."""
    user = db.scalar(select(User).where(User.email == DEV_USER_EMAIL))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Dev user not found. Run the seed SQL from Step 5.0.",
        )
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]