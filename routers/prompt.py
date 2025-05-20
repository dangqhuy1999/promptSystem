from fastapi import APIRouter, HTTPException
from  composer import compose_prompt

router = APIRouter()

@router.get("/{project}/{use_case}")
def get_composed_prompt(project: str, use_case: str):
    try:
        prompt = compose_prompt(project, use_case)
        return {
            "project": project,
            "use_case": use_case,
            "composed_prompt": prompt
        }
    except (FileNotFoundError, ValueError) as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
