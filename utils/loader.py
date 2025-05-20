import os
import yaml

CONFIG_PATH = "configs/prompt_config.yml"
BLOCKS_BASE_PATH = "prompt_blocks"

def load_prompt_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_yaml_block(block_file: str) -> str:
    if not os.path.exists(block_file):
        raise FileNotFoundError(f"Block file not found: {path}")
    with open(block_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data.get("content", "")  # assume YAML block has "content" field

