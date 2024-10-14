from fastapi import FastAPI, HTTPException
from bson import ObjectId
from models import task_collection
from pydantic_schemas import TaskCreate, TaskUpdate, TaskBulkCreate, TaskBulkDelete

app = FastAPI()

# Helper function to serialize MongoDB ObjectId
def serialize_id(id):
    return str(id)

# Create a new task
@app.post("/v1/tasks", status_code=201)
async def create_task(task: TaskCreate):
    task_doc = task.dict()
    new_task = await task_collection.insert_one(task_doc)
    return {"id": serialize_id(new_task.inserted_id)}

# List all tasks
@app.get("/v1/tasks", status_code=200)
async def list_all_tasks():
    tasks = await task_collection.find().to_list(1000)
    return {
        "tasks": [
            {"id": serialize_id(task["_id"]), "title": task["title"], "is_completed": task["is_completed"]}
            for task in tasks
        ]
    }

# Get a specific task
@app.get("/v1/tasks/{id}", status_code=200)
async def get_task(id: str):
    task = await task_collection.find_one({"_id": ObjectId(id)})
    if task:
        return {"id": serialize_id(task["_id"]), "title": task["title"], "is_completed": task["is_completed"]}
    raise HTTPException(status_code=404, detail="There is no task at that id")

# Update a specific task
@app.put("/v1/tasks/{id}", status_code=204)
async def update_task(id: str, task_update: TaskUpdate):
    task_doc = {k: v for k, v in task_update.dict().items() if v is not None}
    if task_doc:
        update_result = await task_collection.update_one({"_id": ObjectId(id)}, {"$set": task_doc})
        if update_result.matched_count == 0:
            raise HTTPException(status_code=404, detail="There is no task at that id")
    return

# Delete a specific task
@app.delete("/v1/tasks/{id}", status_code=204)
async def delete_task(id: str):
    result = await task_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return

# Bulk create tasks
@app.post("/v1/tasks/bulk", status_code=201)
async def bulk_create_tasks(bulk_tasks: TaskBulkCreate):
    task_docs = [task.dict() for task in bulk_tasks.tasks]
    result = await task_collection.insert_many(task_docs)
    return {"tasks": [{"id": serialize_id(task_id)} for task_id in result.inserted_ids]}

# Bulk delete tasks
@app.delete("/v1/tasks/bulk", status_code=204)
async def bulk_delete_tasks(bulk_delete: TaskBulkDelete):
    ids_to_delete = [ObjectId(task_id) for task_id in bulk_delete.tasks]
    result = await task_collection.delete_many({"_id": {"$in": ids_to_delete}})
    return
