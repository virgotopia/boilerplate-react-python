from fastapi import Cookie, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Optional
from app.core.security import verify_session_token
from app.db.database import get_db
from app.models.user import User


def get_current_user(
    session_token: Optional[str] = Cookie(None),
    db: Session = Depends(get_db)
) -> User:
    """Dependency to get the current authenticated user."""
    if not session_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user_id = verify_session_token(session_token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid or expired session")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user
