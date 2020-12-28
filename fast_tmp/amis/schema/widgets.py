from pydantic.main import BaseModel


class Column(BaseModel):
    name: str
    label: str
