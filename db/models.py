from sqlalchemy.orm import (
    mapped_column,
    Mapped,
)
from sqlalchemy import String, Boolean

from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(128), nullable=False)
    last_name: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    def __str__(self):
        return f'User(user_id={self.user_id}, username="{self.username}", first_name="{self.first_name}", last_name="{self.last_name}")'

    def __repr__(self):
        return f'User(user_id={self.user_id}, username="{self.username}", first_name="{self.first_name}", last_name="{self.last_name}")'
