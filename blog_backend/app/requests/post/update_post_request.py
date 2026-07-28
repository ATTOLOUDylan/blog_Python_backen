from pydantic import BaseModel


class UpdatePostRequest(BaseModel):
    title: str | None = None
    content: str | None = None
