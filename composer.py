from typing import List, Dict, Any

def compose_prompt(blocks: List[Dict[str, Any]], context: Dict[str, Any] = None) -> str:
    prompt_parts = []
    # Ví dụ: mỗi block có "content" hoặc "template"
    for block in blocks:
        content = block.get("content", "")
        # Nếu block có template và context, render template
        if "{context" in content and context:
            content = content.format(context=context)
        prompt_parts.append(content)
    
    # Nếu có thêm context chung thì thêm ở cuối prompt
    if context:
        prompt_parts.append(f"\nContext:\n{context}")
    
    return "\n\n".join(prompt_parts)

