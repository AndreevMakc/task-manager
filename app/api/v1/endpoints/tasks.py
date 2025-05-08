from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.models.task import Task
from app.schemas.task import Task as TaskSchema
from app.schemas.task import TaskCreate, TaskUpdate
from app.schemas.task_status import TaskStatus
from app.services.task_service import TaskService

router = APIRouter()


@router.get("/", response_model=List[TaskSchema])
def read_tasks(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    task_service = TaskService(db)
    return task_service.get_tasks(skip=skip, limit=limit)


@router.post("/", response_model=TaskSchema)
def create_task(
    *,
    db: Session = Depends(get_db),
    task_in: TaskCreate
):
    task_service = TaskService(db)
    return task_service.create_task(task_in)


@router.get("/{task_id}", response_model=TaskSchema)
def read_task(
    *,
    db: Session = Depends(get_db),
    task_id: str
):
    task_service = TaskService(db)
    return task_service.get_task(task_id)


@router.put("/{task_id}", response_model=TaskSchema)
def update_task(
    *,
    db: Session = Depends(get_db),
    task_id: str,
    task_in: TaskUpdate
):
    task_service = TaskService(db)
    return task_service.update_task(task_id, task_in)


@router.patch("/{task_id}/status", response_model=TaskSchema)
def update_task_status(
    *,
    db: Session = Depends(get_db),
    task_id: str,
    status: TaskStatus
):
    task_service = TaskService(db)
    return task_service.update_task_status(task_id, status)


@router.delete("/{task_id}")
def delete_task(
    *,
    db: Session = Depends(get_db),
    task_id: str
):
    task_service = TaskService(db)
    task_service.delete_task(task_id)
    return {"ok": True}
