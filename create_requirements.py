from pathlib import Path

ROOT = Path(__file__).resolve().parent

print(f"Creating project structure in: {ROOT}")

assert ROOT.name == "amtsklar", (
    f"Expected project root to be 'amtsklar', got '{ROOT.name}'"
)
requirements = """
fastapi
uvicorn[standard]
python-multipart
pydantic
pydantic-settings

openai

pdfplumber
pymupdf
pytesseract
pillow

python-dotenv

sqlalchemy

pytest
httpx

pyyaml

rich
""".strip()

(ROOT / "requirements.txt").write_text(
    requirements,
    encoding="utf-8"
)

print("✅ requirements.txt created.")