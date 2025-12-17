from pydantic import BaseModel, Field, field_validator, ConfigDict  #type: ignore
from typing import Optional
from bson.objectid import ObjectId  #type: ignore

class Project(BaseModel):
    # 1. NEW: Configuration via ConfigDict
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True
    )

    id: Optional[ObjectId] = Field(default=None, alias="_id")
    project_id: str = Field(..., min_length=1)

    # 2. NEW: Use @field_validator instead of @validator
    @field_validator("project_id")
    @classmethod
    def validate_project_id(cls, value: str):
        if not value.isalnum():
            raise ValueError("project_id must be alphanumeric!")
        return value