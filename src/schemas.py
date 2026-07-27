from pydantic import BaseModel, Field

class Category(BaseModel):
    id: int
    name: str

class MenuItem(BaseModel):
    id: int
    name: str
    price: float
    category: Category