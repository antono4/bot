"""File Operations Module"""
from pathlib import Path

class FileOperations:
    def read_file(self, path):
        try:
            p = Path(path)
            if not p.exists():
                return f"File not found: {path}"
            return p.read_text(encoding="utf-8")
        except Exception as e:
            return f"Error: {e}"
    
    def write_file(self, path, content):
        try:
            p = Path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
            return f"File written: {path}"
        except Exception as e:
            return f"Error: {e}"
    
    def list_files(self, path="."):
        try:
            p = Path(path)
            if not p.is_dir():
                return f"Not a directory: {path}"
            items = [f"  {\'d\' if i.is_dir() else \'f\'} {i.name}" for i in sorted(p.iterdir())]
            return "\n".join(items) if items else "Empty"
        except Exception as e:
            return f"Error: {e}"
