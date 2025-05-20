import yaml
from utils.loader import load_yaml_block 
import os

def compose_prompt(project: str, use_case: str, config_path="configs/prompt_config.yml") -> str:
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    if project not in config or use_case not in config[project]:
        raise ValueError("Invalid project or use_case")

    blocks = config[project][use_case]
    full_prompt = []

    for block_file in blocks:
        block_path = os.path.join("prompt_blocks", project, use_case, block_file)
        content = load_yaml_block(block_path)
        full_prompt.append(content.strip())

    return "\n\n".join(full_prompt)

