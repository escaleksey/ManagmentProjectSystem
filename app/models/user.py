from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.extentions import db

class User(db.Model):
    __tablename__ = 'users'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sa.String(64), index=True, unique=True)
    about: orm.Mapped[str] = orm.mapped_column(sa.String(255))
    email: orm.Mapped[str] = orm.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: orm.Mapped[Optional[str]] = orm.mapped_column(sa.String(256))

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

