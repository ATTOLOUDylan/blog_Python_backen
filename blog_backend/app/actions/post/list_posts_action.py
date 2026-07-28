from sqlalchemy.orm import joinedload

from app.config.database import SessionLocal
from app.models.post import Post


def list_posts_action(
    search: str | None = None,
    author_id: int | None = None,
    skip: int = 0,
    limit: int = 10,
):
    db = SessionLocal()
    try:
        query = db.query(Post).options(joinedload(Post.author), joinedload(Post.likes))

        if search:
            query = query.filter(
                Post.title.ilike(f"%{search}%") | Post.content.ilike(f"%{search}%")
            )
        if author_id is not None:
            query = query.filter(Post.author_id == author_id)

        posts = query.offset(skip).limit(limit).all()
        return posts
    finally:
        db.close()
