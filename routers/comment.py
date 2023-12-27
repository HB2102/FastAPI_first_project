from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.exceptions import HTTPException
from schemas import CommentDisplay, CommentBase, UserAuth
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_comment
from typing import List
from string import ascii_letters
from auth import auth2
import random
import shutil


router = APIRouter(prefix='/comment', tags=['comment'])




@router.post('/create_comment', response_model=CommentDisplay)
def create_post(request: CommentBase, db: Session = Depends(get_db),
                current_user: UserAuth = Depends(auth2.get_current_user)
                ):

    return db_comment.create_comment(request, db)



@router.post('/delete_comment/{id}')
def delete_comment(id: int, db: Session = Depends(get_db),
                current_user: UserAuth = Depends(auth2.get_current_user)
                ):
    return db_comment.delete_comment(id=id, db=db, user_id=current_user.id)



@router.get('/{id}', response_model=List[CommentDisplay])
def get_comments(id:int, db: Session = Depends(get_db)):
    return db_comment.get_all_comments_by_post_id(id=id, db=db)

