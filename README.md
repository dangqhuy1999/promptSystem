
# 🧠 Prompt System

A modular and configurable **Prompt Management System** for AI applications, enabling flexible composition and reuse of prompt blocks across various projects and use cases.

## 🚀 Key Features

- ✅ **Project-based structure**: Organize prompts by project and use case.
- 🧩 **Modular prompt blocks**: Define reusable prompt blocks in YAML format.
- ⚙️ **Config-driven**: Compose full prompts dynamically using a central config file.
- 🌐 **REST API endpoint**: Expose prompts via HTTP requests for easy integration.
- 🧪 **Simple and testable structure**: Clean separation of loading logic and composition logic.

---

## 📁 Directory Structure

```
promptSystem/
├── configs/
│ └── prompt_config.yml
├── prompt_blocks/
│ └── project1/
│ ├── classification/
│ │ ├── classification_intro.yml
│ │ └── classification_rules.yml
│ └── summarization/
│ ├── intro_block.yml
│ └── summary_block.yml
├── utils/
│ └── loader.py
├── composer.py
└── routers/
└── prompt.py
```

---

## 🛠 How It Works

1. **Prompt Blocks**:

   Each `.yml` file in `prompt_blocks/` contains a single `content:` field with the raw prompt text.

   ```yaml
   # Example of a block
   content: |
     You are an AI assistant trained to classify text.
     Follow the rules carefully before responding.
    Configuration:
     The configs/prompt_config.yml maps which blocks to include for each         project/use_case combination.

```yaml
project1:
  classification:
    - classification_intro.yml
    - classification_rules.yml
```

Composing Prompts:

The system reads the config, loads and concatenates block content, and returns the final composed prompt.

## 🔌 API Usage

GET /get_prompt/{project}/{use_case}

Example:

```bash
curl -X GET http://localhost:8789/get_prompt/project1/classification
```

Response:

```text
You are an AI assistant trained to classify text.

Classification Rules:
- Class 1: ...
- Class 2: ...
```

## 📦 Dependencies

```
Python 3.10+
FastAPI
PyYAML
```

## ✅ TODO / Ideas
 
 Admin UI to manage and edit blocks.

 Validation schema for prompt YAML files.

 Caching system for composed prompts.

 Versioning support for prompts.

## 👨‍💻 Author

Built with ❤️ by HUY.
