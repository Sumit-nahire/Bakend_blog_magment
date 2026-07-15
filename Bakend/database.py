# SQLAlchemy se required modules import kar rahe hain
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# PostgreSQL database ka connection URL
# Format:
# postgresql://username:password@host/database_name
#DATABASE_URL = "postgresql://postgres:root@localhost/blogdb"
DATABASE_URL=os.getenv("DATABASE_URL")

# Database ke saath connection establish karne ke liye Engine create hota hai
# Engine SQLAlchemy aur database ke beech bridge ki tarah kaam karta hai
engine = create_engine(DATABASE_URL)

# Session create karne ka factory object
# Session ka use database me CRUD operations (Create, Read, Update, Delete) ke liye hota hai
SessionLocal = sessionmaker(bind=engine)

# Base class create karte hain
# Is Base ko inherit karke hum apne database models (tables) banate hain
Base = declarative_base()