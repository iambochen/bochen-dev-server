from fastapi import FastAPI, BackgroundTasks
from worker.tasks import add, multiply

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add")
async def add_numbers(x: int, y: int, background_tasks: BackgroundTasks):
    """Add two numbers asynchronously using Celery."""
    task = add.delay(x, y)
    background_tasks.add_task(lambda: task.get())
    return {"task_id": str(task.id)}

@app.post("/multiply")
async def multiply_numbers(x: int, y: int, background_tasks: BackgroundTasks):
    """Multiply two numbers asynchronously using Celery."""
    task = multiply.delay(x, y)
    background_tasks.add_task(lambda: task.get())
    return {"task_id": str(task.id)}
