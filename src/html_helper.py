import base64
from . import config
from .schemas import MenuItem
from pyhtml2pdf import converter
from .file_helper import read_file

def get_section_html(title: str) -> str:
    """
    Helper methods to quickly retrieve the HTML node for a section in the menu
    """
    return f"""
        <div class="menu-section">
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

def _font_data_uri(file_name: str) -> str:
    """
    Base64-encodes a font file so it can be embedded directly in the CSS.
    Needed because the PDF conversion step loads the HTML as a data: URL,
    which has no filesystem location to resolve relative font paths against.
    """
    data = (config.RESOURCES_DIR / file_name).read_bytes()
    return f"data:font/ttf;base64,{base64.b64encode(data).decode('ascii')}"

def get_inline_stylesheet() -> str:
    """
    Loads style.css with its @font-face urls replaced by inline data URIs.
    """
    css = read_file(config.RESOURCES_DIR / "style.css")
    return (
        css
        .replace("BrolimoRegular.ttf", _font_data_uri("BrolimoRegular.ttf"))
        .replace("Montserrat-Regular.ttf", _font_data_uri("Montserrat-Regular.ttf"))
    )

def build_document(items_html: str) -> str:
    """
    Assembles the full printable HTML: injects the items into the template
    and inlines the stylesheet (fonts included) in place of the external
    <link>, since the conversion step can't resolve external files.
    """
    html = read_file(config.HTML_FILE)
    html = html.replace('<div class="items-container"></div>', items_html)
    html = html.replace(
        '<link rel="stylesheet" href="style.css" />',
        f'<style>{get_inline_stylesheet()}</style>',
    )
    return html

def convert_html_to_pdf(html: str) -> None:
    """
    Converts an HTML string to a .pdf file. Output file is saved on the configured path.
    """
    converter.convert(html, config.OUTPUT_PDF_FILE)
