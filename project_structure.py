from pathlib import Path

ROOT = Path("amtsklar")

directories = [
    "frontend",
    "backend",
    "backend/app",
    "backend/app/api",
    "backend/app/core",
    "backend/app/services",
    "backend/app/models",
    "backend/app/utils",
    "backend/tests",
    "data",
    "data/samples",
    "data/schemas",
    "data/prompts",
    "knowledge",
    "knowledge/rundfunk",
    "scripts",
]

files = {
    "README.md": "# Amtsklar\n",
    ".gitignore": "",
    ".env.example": "",
    "backend/app/main.py": "",
    "backend/app/__init__.py": "",
    "backend/app/api/__init__.py": "",
    "backend/app/core/__init__.py": "",
    "backend/app/services/__init__.py": "",
    "backend/app/models/__init__.py": "",
    "backend/app/utils/__init__.py": "",
    "backend/tests/__init__.py": "",
    "knowledge/rundfunk/document_types.yaml": "",
    "knowledge/rundfunk/workflows.yaml": "",
    "knowledge/rundfunk/field_definitions.yaml": "",
    "knowledge/rundfunk/faq.yaml": "",
}

print("Creating directory structure...")

for directory in directories:
    (ROOT / directory).mkdir(parents=True, exist_ok=True)

for file, content in files.items():
    path = ROOT / file
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text(content, encoding="utf-8")

print("✅ Amtsklar project structure created.")