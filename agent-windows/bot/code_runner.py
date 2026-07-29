"""Python Code Runner Module"""
import io, sys
from contextlib import redirect_stdout, redirect_stderr

class CodeRunner:
    def run(self, code):
        if not code:
            return "Code is empty"
        try:
            f = io.StringIO()
            with redirect_stdout(f), redirect_stderr(f):
                exec(code, {"__name__": "__main__"})
            out = f.getvalue()
            return out if out else "Code executed (no output)"
        except SyntaxError as e:
            return f"Syntax Error: {e}"
        except Exception as e:
            return f"Error: {e}"
