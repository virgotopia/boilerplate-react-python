import bcrypt
from itsdangerous import URLSafeTimedSerializer
from typing import Optional

SECRET_KEY = "your-secret-key-change-in-production"
SERIALIZER = URLSafeTimedSerializer(SECRET_KEY)


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )


def create_session_token(user_id: int) -> str:
    """Create a session token for a user."""
    return SERIALIZER.dumps({"user_id": user_id})


def verify_session_token(token: str) -> Optional[int]:
    """Verify a session token and return the user_id."""
    try:
        data = SERIALIZER.loads(token, max_age=86400 * 7)  # 7 days
        return data.get("user_id")
    except:
        return None
