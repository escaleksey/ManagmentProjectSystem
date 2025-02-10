from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from werkzeug.security import check_password_hash, generate_password_hash

from app.extentions import db


class User(db.Model):
    __tablename__ = "users"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(
        sa.String(64), index=True, unique=True
    )
    about: orm.Mapped[str] = orm.mapped_column(sa.String(255))
    email: orm.Mapped[str] = orm.mapped_column(sa.String(120), index=True, unique=True)
    _password_hash: orm.Mapped[Optional[str]] = orm.mapped_column(sa.String(256))

    def __repr__(self) -> str:
        return f"<User(username={self.username}, email={self.email})>"

    @property
    def password(self) -> str:
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password: str) -> None:
        self._password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self._password_hash, password)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "about": self.about,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
