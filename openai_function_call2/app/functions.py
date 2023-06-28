import requests
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    task: str
    is_completed: bool


def get_todos(completed=None):
    params = {"completed": completed} if completed is not None else None
    response = requests.get(
        "https://fastapilangchain-1-w0858112.deta.app/todos", params=params
    )
    return response.json()


def create_todo(todo: Todo):
    response = requests.post(
        "https://fastapilangchain-1-w0858112.deta.app/todos", json=todo
    )
    return response.json()


def update_todo(id: int, todo: Todo):
    response = requests.put(
        f"https://fastapilangchain-1-w0858112.deta.app/todos/{id}", json=todo
    )
    return response.json()


def delete_todo(id: int):
    response = requests.delete(
        f"https://fastapilangchain-1-w0858112.deta.app/todos/{id}"
    )
    return response.status_code


api_functions = {
    "get_todos": get_todos,
    "create_todo": create_todo,
    "update_todo": update_todo,
    "delete_todo": delete_todo,
}
