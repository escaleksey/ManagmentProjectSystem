from typing import Optional
from datetime import datetime
import sqlalchemy as sa
import sqlalchemy.orm as orm

from app.extentions import db


class Project(db.Model):
    __tablename__ = "project"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(
        sa.String(64), index=True
    )
    theme: orm.Mapped[str] = orm.mapped_column(sa.String(255))
    creating_date: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime(), index=True)
    project_roles = orm.relationship("ProjectMemberRole", back_populates="project")
    tasks = orm.relationship("Task", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Project(title={self.title})>"


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "theme": self.theme,
            "date": self.creating_date.isoformat() if self.creating_date else None,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
