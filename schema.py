from pydantic import BaseModel
from typing import Optional




class Parameters(BaseModel):
    price_filter: Optional[str] = None
    search: Optional[str] = None
    os: Optional[str] = None
    tag: Optional[str] = None
    language: Optional[str] = None
    is_special_offer: Optional[bool] = None