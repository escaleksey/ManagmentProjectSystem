from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy as sa
import sqlalchemy.orm as orm

from app.extentions import db


class Task(db.Model):
    __tablename__ = "task"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(
        sa.String(64), index=True
    )
    description: orm.Mapped[str] = orm.mapped_column(sa.String(255))

    # Связь с проектом
    project_id: orm.Mapped[int] = orm.mapped_column(ForeignKey('project.id'))
    stage_id: orm.Mapped[int] = orm.mapped_column(ForeignKey('stage.id'), default=1)

    # Определяем связи с проектом
    project = relationship("Project", back_populates="tasks")
    stage = relationship("Stage", back_populates="tasks")


    def __repr__(self):
        return (f"<Task(id={self.id}, title={self.title}, description={self.description},"
                f" project_id={self.project_id}, stage_id={self.stage_id})>")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "project_id": self.project_id,
            "stage_id": self.stage_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
