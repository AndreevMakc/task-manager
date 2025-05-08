from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.schemas.task_status import TaskStatus


class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def get_tasks(self, skip: int = 0, limit: int = 100) -> List[Task]:
        return self.db.query(Task).offset(skip).limit(limit).all()

    def get_task(self, task_id: str) -> Task:
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def create_task(self, task_in: TaskCreate) -> Task:
        task = Task(**task_in.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: str, task_in: TaskUpdate) -> Task:
        task = self.get_task(task_id)

        update_data = task_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task_status(self, task_id: str, status: TaskStatus) -> Task:
        task = self.get_task(task_id)
        task.status = status
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        self.db.delete(task)
        self.db.commit()
        return True
