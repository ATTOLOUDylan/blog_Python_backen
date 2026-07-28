from sqlalchemy.orm import joinedload

from app.config.database import SessionLocal
from app.models.comment import Comment
from app.models.post import Post
from app.models.user import User
from app.requests.comment.create_comment_request import CreateCommentRequest


def create_comment_action(post_id: int, data: CreateCommentRequest, author: User):
    db = SessionLocal()
    try:
        post = db.query(Post).filter(Post.id == post_id).first()
        if post is None:
            return None

        comment = Comment(
            content=data.content,
            author_id=author.id,
            post_id=post_id,
        )
        db.add(comment)
        db.commit()
        db.refresh(comment)
        comment = (
            db.query(Comment)
            .options(joinedload(Comment.author))
            .filter(Comment.id == comment.id)
            .first()
        )
        return comment
    finally:
        db.close()
