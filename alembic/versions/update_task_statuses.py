"""update task statuses

Revision ID: update_task_statuses
Revises: 
Create Date: 2024-03-19

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'update_task_statuses'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Обновляем значения статусов
    op.execute("""
        UPDATE tasks 
        SET status = CASE 
            WHEN status = 'todo' THEN 'To Do'
            WHEN status = 'in_progress' THEN 'In Progress'
            WHEN status = 'done' THEN 'Done'
            WHEN status = 'cancelled' THEN 'Cancelled'
            ELSE status
        END
    """)


def downgrade():
    # Возвращаем старые значения
    op.execute("""
        UPDATE tasks 
        SET status = CASE 
            WHEN status = 'To Do' THEN 'todo'
            WHEN status = 'In Progress' THEN 'in_progress'
            WHEN status = 'Done' THEN 'done'
            WHEN status = 'Cancelled' THEN 'cancelled'
            ELSE status
        END
    """)
