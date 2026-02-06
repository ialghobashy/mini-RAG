from pydantic import BaseModel # type: ignore
from typing import Optional

class PushRequest(BaseModel):
    do_reset: Optional[int] = 0

