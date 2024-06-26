from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database connection URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create a new SQLAlchemy engine instance
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the ORM models
Base = declarative_base()

def create_all_tables():
    """
    Create all tables in the database.
    """
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Run the function to create all tables when the script is executed directly
    create_all_tables()
