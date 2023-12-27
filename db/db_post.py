import datetime
from db.models import Post
from schemas import PostBase
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status



def create_post(request: PostBase, db :Session):
    new_post = Post(
        image_url= request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.datetime.now(),
        user_id = request.creator_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db: Session):
    return db.query(Post).all()



def delete_post(id: int, db: Session, user_id: int):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if not post.user_id == user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    db.delete(post)
    db.commit()
    return 'post deleted'
