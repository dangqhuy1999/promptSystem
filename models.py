from pydantic import BaseModel
from typing import Optional, Dict, Any

class PromptRequest(BaseModel):
    project_id: str
    use_case: str
    context: Optional[Dict[str, Any]] = None  # context tu sheet, qdrant, redis

class PromptResponse(BaseModel):
    prompt: str

