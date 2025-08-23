from typing import Annotated

from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: Annotated[int, Field(title="Employee Id", examples=[1, 2, 3])]
    name: Annotated[str, Field(title="Employee Name", examples=["Bibek", "Harry", "Salman"])]
    department: Annotated[str, Field(title="Employee Department", examples=["AI", "Designer", "Marketing"])]
    age: Annotated[int, Field(title="Employee Id", examples=[31, 42, 23])]