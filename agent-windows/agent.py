"""Windows Agent - Main Entry Point"""
import os, sys, json, argparse
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from config import MODEL, TEMPERATURE, MAX_TOKENS, SAVE_HISTORY, HISTORY_FILE
from bot.chat import ChatBot
from bot.file_ops import FileOperations
from bot.web import WebSearch
from bot.code_runner import CodeRunner
from bot.windows_auto import WindowsAutomation


class WindowsAgent:
    def __init__(self):
        self.chat = ChatBot()
        self.files = FileOperations()
        self.web = WebSearch()
        self.code = CodeRunner()
        self.windows = WindowsAutomation()
        self.history = []
        
        if SAVE_HISTORY and Path(HISTORY_FILE).exists():
            try:
                with open(HISTORY_FILE, 'r') as f:
                    self.history = json.load(f)
            except:
                pass
    
    def save_history(self):
        if SAVE_HISTORY:
            with open(HISTORY_FILE, 'w') as f:
                json.dump(self.history, f, indent=2)
    
    def process(self, cmd):
        cmd_lower = cmd.lower().strip()
        
        if cmd_lower.startswith("baca file "):
            return self.files.read_file(cmd[10:].strip())
        if cmd_lower.startswith("tulis file "):
            parts = cmd[11:].split("|", 1)
            if len(parts) >= 2:
                return self.files.write_file(parts[0].strip(), parts[1].strip())
            return "Format: tulis file <path> | <content>"
        if cmd_lower.startswith("list file "):
            return self.files.list_files(cmd[10:].strip() or ".")
        if cmd_lower == "list file":
            return self.files.list_files(".")
        if cmd_lower.startswith("cari "):
            return self.web.search(cmd[5:].strip())
        if cmd_lower.startswith("jalankan "):
            return self.code.run(cmd[9:].strip())
        if cmd_lower.startswith("click "):
            parts = cmd[6:].strip().split()
            if len(parts) >= 2:
                return self.windows.click(int(parts[0]), int(parts[1]))
            return self.windows.click()
        if cmd_lower.startswith("move "):
            parts = cmd[5:].strip().split()
            if len(parts) >= 2:
                return self.windows.move_mouse(int(parts[0]), int(parts[1]))
            return "Format: move <x> <y>"
        if cmd_lower.startswith("screenshot"):
            fname = cmd[11:].strip() or "screenshot.png"
            return self.windows.screenshot(fname)
        if cmd_lower.startswith("wait "):
            return self.windows.wait(float(cmd[5:].strip()))
        
        return self.chat.ask(cmd, self.history)
    
    def run_interactive(self):
        print("=" * 50)
        print("Windows Agent - AI Automation")
        print("=" * 50)
        print("Commands: baca file, tulis file, list file")
        print("          cari, jalankan, screenshot, click, move")
        print("          exit untuk keluar")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                if not user_input:
                    continue
                if user_input.lower() in ["exit", "quit", "keluar"]:
                    print("Bye!")
                    break
                
                self.history.append({"role": "user", "content": user_input})
                response = self.process(user_input)
                self.history.append({"role": "assistant", "content": response})
                print(f"AI: {response}")
                
            except KeyboardInterrupt:
                print("\nBye!")
                break
            except Exception as e:
                print(f"Error: {e}")
        
        self.save_history()
    
    def run_task(self, task):
        print(f"Running: {task}")
        result = self.process(task)
        print(f"Result: {result}")
        return result


def main():
    parser = argparse.ArgumentParser(description="Windows AI Agent")
    parser.add_argument("--task", "-t", type=str, help="Single task")
    args = parser.parse_args()
    
    agent = WindowsAgent()
    
    if args.task:
        agent.run_task(args.task)
    else:
        agent.run_interactive()


if __name__ == "__main__":
    main()
