from pydantic import BaseModel


class Environments(BaseModel):
    environment: str
