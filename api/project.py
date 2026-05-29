from pathlib import Path

import pwndbg
from .process import Process

class Project:
    """
    Instantiates an object for the binary/process to be debugged.
    """
    def __init__(self, binary_path: Path, args: list[str] = []):
        self.binary_path = binary_path
        self.args: list[str] = args
        self.env: dict[str, str] = {}
        self.arch = pwndbg.dbg.selected_inferior().arch

    def __str__(self) -> str:
        return ""

    def set_env(self, env: dict[str, str]) -> None:
        self.env = env

    def run(self) -> Process:
        return Process(self)
