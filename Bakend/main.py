from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas
from auth import create_token, verify_token
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog Management System")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://blog-magment-fortend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Login API
@app.post("/login")
def login():
    return {
        "access_token": create_token({"user": "admin"}),
        "token_type": "bearer"
    }


# Home
@app.get("/")
def home():
    return {
        "message": "blog api started"
    }


# Create Blog (protected)
@app.post("/blogs", response_model=schemas.BlogResponse)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db), user=Depends(verify_token)):
    new_blog = models.Blog(
        title=blog.title,
        content=blog.content
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


# Read all
@app.get("/blogs")
def get_blogs(page: int = 1,
              limit: int = 5,
              search: str = Query(default=""),
              db: Session = Depends(get_db)):
    query = db.query(models.Blog)
    if search:
        query = query.filter(models.Blog.title.ilike(f"%{search}%"))

    total = query.count()
    start = (page - 1) * limit
    blogs = query.offset(start).limit(limit).all()
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": blogs
    }


# Update Blog API
@app.put("/blogs/{id}", response_model=schemas.BlogResponse)
def update_blog(id: int, blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not existing_blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    existing_blog.title = blog.title
    existing_blog.content = blog.content

    db.commit()
    return existing_blog


# Delete Blog API
@app.delete("/blogs/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=404, detail="Blog not found")

    blog.delete()
    db.commit()

    return {
        "message": "Blog Deleted Successfully"
    }