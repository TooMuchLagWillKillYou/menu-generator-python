import csv
from src import config
from src.schemas import MenuItem
from src.html_helper import read_index, get_item_html

def get_items() -> list[MenuItem]:
    with open(config.ITEMS_FILE, newline='', encoding='cp1252') as f:
        reader = csv.DictReader(f, delimiter=',')
        return [MenuItem(**row) for row in reader]

def compose_items() -> str:

    result = '<div class="items-container">'
    result += ''.join(get_item_html(item) for item in get_items())
    result += '</div>'

    return result

def main():
    html = read_index(config.HTML_FILE)

    items_html = compose_items()
    new_html = html.replace('<div class="items-container"></div>', items_html)
    print(new_html)

if __name__ == "__main__":
    main()