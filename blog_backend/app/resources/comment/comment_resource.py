from datetime import datetime

from pydantic import BaseModel


class CommentResource(BaseModel):
    id: int
    content: str
    created_at: datetime
    author_id: int
    author_name: str
    post_id: int

    class Config:
        from_attributes = True

    @classmethod
    def from_comment(cls, comment):
        return cls(
            id=comment.id,
            content=comment.content,
            created_at=comment.created_at,
            author_id=comment.author_id,
            author_name=comment.author.name,
            post_id=comment.post_id,
        )
