import csv
from src import config
from src.schemas import MenuItem
from src.html_helper import get_item_html, build_document, convert_html_to_pdf
from src.file_helper import write_file

def get_items() -> list[MenuItem]:
    with open(config.ITEMS_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        return [MenuItem(**row) for row in reader]

def compose_items() -> str:

    result = '<div class="items-container">'
    result += ''.join(get_item_html(item) for item in get_items())
    result += '</div>'

    return result

def main():
    html = build_document(compose_items())
    write_file(config.OUTPUT_HTML_FILE, html)
    convert_html_to_pdf(html)

if __name__ == "__main__":
    main()
