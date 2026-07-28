from pyhtml2pdf import converter
import os

def write_front_page():
    pass

def write_specialty():
    pass

def write_classic():
    pass

def main():
    path = os.path.abspath("index.html")
    converter.convert(f'file://{path}', './result.pdf')
    print("Hello world")

if __name__ == "__main__":
    main()