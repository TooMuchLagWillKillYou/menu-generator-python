from . import config
from .schemas import MenuItem
from pyhtml2pdf import converter

def get_page_html(title: str) -> str:
    """
    Helper methods to quickly retrieve the HTML node for a page in the menu
    """
    return f"""
        <div class="page">
            <h1 class="section-title">{title}</h1>
            <div class="items-container"></div>
        </div>
"""

def get_item_html(item: MenuItem) -> str:
    """
    Helper methods to quickly retrieve the HTML node for an item in the menu
    """
    return f"""
        <div class="item">
            <div class="item-header">
                <h2 class="item-title">{item.name}</h2>
                <p class="item-price">{item.first_price}</p>
            </div>
            <p class="item-description">
                {item.ingredients}
            </p>
        </div>
"""

def read_index(file_path) -> str:
    """
    Reads a file and puts its content in memory 
    """
    with open(file_path, "r", encoding='utf-8') as f:
        return f.read()

def convert_html_to_pdf(html: str) -> None:
    """
    Converts an HTML string to a .pdf file. Output file is saved on the configured path.
    """
    converter.convert(html, config.OUTPUT_FILE)