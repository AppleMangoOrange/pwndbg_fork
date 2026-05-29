import dataclasses
from typing import Any, Literal, Optional

import pwndbg
from .project import Project

@dataclasses.dataclass
class StopReason:
    """
    Show details about stopped/suspended processes.
    """
    type: Literal["breakpoint", "signal", "syscall", "exit", "step"]
    signal: Optional[str] = None
    breakpoint: Optional[Any] = None
    exit_code: Optional[int] = None

class Process:
    """
    Handles active execution state, memory, and stepping.
    """
    def __init__(self, project: Project):
        self.project = project
        self.inferior = pwndbg.dbg.selected_inferior()

    def __str__(self) -> str:
        return ""

    def break_at(self, location: str | int):
        pass

    def continue_until(self, bp: Any) -> StopReason:
        return StopReason("breakpoint")
        pass

    def registers(self) -> Any:
        # Return a typed RegisterState dataclass based on the project's arch
        pass

    def read_memory(self, addr: int, size: int) -> bytes:
        return bytes(self.inferior.read_memory(addr, size))

    def step_instruction(self) -> StopReason:
        return StopReason("breakpoint")
        pass
