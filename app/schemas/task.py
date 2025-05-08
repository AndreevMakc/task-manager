from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID
from .task_status import TaskStatus


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: TaskStatus = TaskStatus.TODO


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class TaskUpdate(TaskBase):
    title: Optional[str] = None
    status: Optional[TaskStatus] = None


class TaskInDBBase(TaskBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Task(TaskInDBBase):
    pass
