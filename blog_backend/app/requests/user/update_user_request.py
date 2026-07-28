from pydantic import BaseModel, EmailStr


class UpdateUserRequest(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
