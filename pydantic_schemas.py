from pydantic import BaseModel
from typing import List, Optional

# For creating a task
class TaskCreate(BaseModel):
    title: str
    is_completed: Optional[bool] = False

# For updating a task
class TaskUpdate(BaseModel):
    title: Optional[str]
    is_completed: Optional[bool]

# For bulk deletion of tasks
class TaskBulkDelete(BaseModel):
    tasks: List[str]  # MongoDB IDs are string-based

# For bulk creation of tasks
class TaskBulkCreate(BaseModel):
    tasks: List[TaskCreate]
