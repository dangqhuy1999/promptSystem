import os
import yaml

CONFIG_PATH = "configs/prompt_config.yml"
BLOCKS_BASE_PATH = "prompt_blocks"

def load_prompt_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_yaml_block(project: str, block_file: str) -> str:
    path = os.path.join(BLOCKS_BASE_PATH, project, block_file)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Block file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data.get("content", "")  # assume YAML block has "content" field

def compose_prompt(project: str, use_case: str) -> str:
    config = load_prompt_config()
    try:
        blocks = config[project][use_case]
    except KeyError:
        raise ValueError("Invalid project or use_case in config.")

    prompt_parts = []
    for block_file in blocks:
        block_content = load_yaml_block(project, block_file)
        prompt_parts.append(block_content)

    return "\n\n".join(prompt_parts)

