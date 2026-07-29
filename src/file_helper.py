def read_file(file_path: str) -> str:
    """
    Reads a file and puts its content in memory
    """
    with open(file_path, "r", encoding='utf-8') as f:
        return f.read()

def write_file(file_path: str, file_content: str) -> None:
    """
    Writes a file in the file system
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)