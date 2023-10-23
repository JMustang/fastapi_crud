from typing import List
from .models import User
from .db import get_db, UserTable

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, db

router = APIRouter()

@router.get("/user", response_model=List[User])
async def get_users(db: Session = Depends(get_db)):
    return db.query(UserTable).all()
# @router.get("/user", response_model=List[models.User])
# async def get_users(db: Session = Depends(db.get_db)):
#     return db.query(models.UserTable).all()

@router.get("/user/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserTable).filter(UserTable.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/user", response_model=User)
async def create_user(user: User, db: Session = Depends(get_db)):
    db_user = UserTable(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/user/{user_id}", response_model=User)
async def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserTable).filter(UserTable.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.patch("/user/{user_id}", response_model=User)
async def patch_user(user_id: int, user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserTable).filter(UserTable.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/user/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserTable).filter(UserTable.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}
