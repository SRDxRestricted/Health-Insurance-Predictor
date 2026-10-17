from pydantic import BaseModel, Field
from typing import Literal


class InsuranceInput(BaseModel):
    age: int = Field(gt=0, le=100)
    sex: Literal["male", "female"]
    bmi: float = Field(gt=0, le=100)
    children: int = Field(ge=0, le=20)
    smoker: Literal["yes", "no"]
    region: Literal[
        "southwest",
        "southeast",
        "northwest",
        "northeast"
    ]