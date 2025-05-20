# main.py
from fastapi import FastAPI, HTTPException
from routers.prompt import router as prompt_router

app = FastAPI(title="Prompt API Server")

app.include_router(prompt_router, prefix="/get_prompt")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8789, reload=True)
# Folder structure:
# ├── main.py
# ├── routes/
# │   └── prompt.py
# ├── utils/
# │   └── loader.py
# └── prompt_blocks/
#     ├── project1/
#     │   ├── intro.txt
#     │   ├── outro.txt
#     │   └── jd_section.txt
#     └── project2/
#         └── ...

# Example Request:
# GET /get_prompt/project1/intro
# Response:
# {"project": "project1", "block": "intro", "prompt": "<content of intro.txt>"}

