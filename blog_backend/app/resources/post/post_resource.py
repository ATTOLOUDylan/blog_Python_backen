from datetime import datetime

from pydantic import BaseModel


class PostResource(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    author_id: int
    author_name: str
    likes_count: int

    class Config:
        from_attributes = True

    @classmethod
    def from_post(cls, post):
        return cls(
            id=post.id,
            title=post.title,
            content=post.content,
            created_at=post.created_at,
            author_id=post.author_id,
            author_name=post.author.name,
            likes_count=len(post.likes),
        )
