from sqlalchemy.orm import Session

from .models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(
        self, first_name: str, username: str, last_name: str | None = None
    ) -> User:
        existing_user = self.session.query(User).filter_by(username=username).all()

        if existing_user:
            print("username already exists.")
            return

        user = User(first_name=first_name, username=username, last_name=last_name)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user

    def get_all_users(self) -> list[User]:
        users = self.session.query(User).all()

        return users

    def get_one_user(self, user_id: int) -> User:
        user = self.session.query(User).get(user_id)

        return user

    def get_active_users(self) -> list[User]:
        users = self.session.query(User).filter_by(is_active=True).all()

        return users
