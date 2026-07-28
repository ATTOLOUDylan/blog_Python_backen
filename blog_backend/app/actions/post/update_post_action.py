from sqlalchemy.orm import joinedload

from app.config.database import SessionLocal
from app.models.post import Post
from app.models.user import User
from app.policies.post.post_policy import authorize_modify_post
from app.requests.post.update_post_request import UpdatePostRequest


def update_post_action(post_id: int, data: UpdatePostRequest, current_user: User):
    db = SessionLocal()
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if post is None:
            return None

        authorize_modify_post(current_user, post)

        if data.title is not None:
            post.title = data.title
        if data.content is not None:
            post.content = data.content

        db.commit()
        db.refresh(post)
        post = (
            db.query(Post)
            .options(joinedload(Post.author), joinedload(Post.likes))
            .filter(Post.id == post.id)
            .first()
        )
        return post
    finally:
        db.close()
