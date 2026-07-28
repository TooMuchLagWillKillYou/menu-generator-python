import os
import csv
from pyhtml2pdf import converter
from src import config
from src.schemas import MenuItem

def get_items() -> list[MenuItem]:
    with open(config.ITEM_FILE, newline='', encoding='cp1252') as f:
        reader = csv.DictReader(f, delimiter=',')
        return [MenuItem(**row) for row in reader]

def convert_html_to_pdf() -> None:
    path = os.path.abspath("./resources/index.html")
    converter.convert(f'file://{path}', config.OUTPUT_FILE)

def main():
        
    items = get_items()
    for item in items[:10]:
        print(item)
        print("\n")

if __name__ == "__main__":
    main()