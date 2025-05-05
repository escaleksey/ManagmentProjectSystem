from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy as sa
import sqlalchemy.orm as orm

from app.extentions import db


class ProjectMemberRole(db.Model):
    __tablename__ = "project_member_role"

    # Связь с пользователем
    user_id: orm.Mapped[int] = orm.mapped_column(ForeignKey('users.id'), primary_key=True)

    # Связь с проектом
    project_id: orm.Mapped[int] = orm.mapped_column(ForeignKey('project.id'), primary_key=True)

    # Роль участника проекта
    role_id: orm.Mapped[str] = orm.mapped_column(ForeignKey('role.id'), nullable=True)

    # Определяем связи с пользователем и проектом
    user = relationship("User", back_populates="project_roles")
    project = relationship("Project", back_populates="project_roles")
    role = relationship("Role", back_populates="project_roles")

    def __repr__(self):
        return f"<ProjectMemberRole(user_id={self.user_id}, project_id={self.project_id}, role={self.role_id})>"

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "project_id": self.project_id,
            "role": self.role_id,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
