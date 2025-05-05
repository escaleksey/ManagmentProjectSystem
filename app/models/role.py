from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.extentions import db


class Role(db.Model):
    __tablename__ = "role"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(
        sa.String(64), index=True, unique=True
    )

    project_roles = orm.relationship("ProjectMemberRole", back_populates="role")

    def __repr__(self) -> str:
        return f"<Role(title={self.title})>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
