from typing import Optional, Dict, Any
from pydantic import BaseModel

class CaptchaResult(BaseModel):
    solution: Optional[Dict[str, str]] = None
    cost: Optional[float] = None

    def __eq__(self, other: Any) -> bool:
        return self.solution == other
    
    def __ne__(self, other: Any) -> bool:
        return self.solution != other