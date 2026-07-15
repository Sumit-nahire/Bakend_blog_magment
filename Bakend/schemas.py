from pydantic import BaseModel
# Input Schema
# Client jab naya blog create karega,
# tab sirf title aur content bhejega.

class BlogCreate(BaseModel):
    title: str
    content: str


# Output Schema
# API response me id, title aur content return honge.
class BlogResponse(BaseModel):
    id: int
    title: str
    content: str

    # Pydantic v2 configuration
    # SQLAlchemy model object ko directly
    # Pydantic model me convert karne ke liye.
    class Config:
        from_attributes = True