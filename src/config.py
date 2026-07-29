from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = ROOT_DIR / "output"
OUTPUT_PDF_FILE = OUTPUT_DIR / "result.pdf"
OUTPUT_HTML_FILE = OUTPUT_DIR / "index.html"

RESOURCES_DIR = ROOT_DIR / "resources"
ITEMS_FILE = RESOURCES_DIR / "datasource_20260425.csv"
HTML_FILE = RESOURCES_DIR / "index.html"