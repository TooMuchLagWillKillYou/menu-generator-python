from pydantic import BaseModel, Field

class Category(BaseModel):
    id: int
    name: str

class MenuItem(BaseModel):
    id: int
    name: str
    ingredients: str
    english_translation: str
    german_translation: str
    # first_price: float
    # second_price: float