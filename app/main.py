from fastapi import FastAPI
# from sqlalchemy import text

from app.config import settings
from app.database import SessionDep


app = FastAPI(title=settings.app_name, debug=settings.debug)

# @app.get("/")
# async def read_root(db: SessionDep = Depends(SessionDep)):
#     result = db.execute(text("SELECT 'Hello, World!'"))
#     return {"message": result.fetchone()[0]}

@app.get("/")
def root():
    result = {"message": f"Hello, {settings.app_name}!"}
    return result

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/db")
def health_db(db: SessionDep):
    mysql_db_version = db.execute(text("SELECT VERSION()")).scalar()
    return {"database": "ok", "mysql_version": mysql_db_version}