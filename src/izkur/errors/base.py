# -*- coding: utf-8 -*-
"""izkur/errors/base.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from dataclasses import dataclass
from typing import Optional, Literal

__all__ = ["ParseError"]

ErrorSeverity = Literal["info", "warning", "error", "critical"]
ErrorStage = Literal["lexical", "syntactic", "semantic", "runtime"]


@dataclass
class ParseError(BaseException):
    message: str
    stage: ErrorStage
    severity: ErrorSeverity = "error"
    source_text: Optional[str] = None
    position: Optional[int] = None  # character offset
    hint: Optional[str] = None

    def __str__(self) -> str:
        location = f" at position {self.position}" if self.position is not None else ""
        return (
            f"[{self.stage.upper()}] {self.severity.upper()}: {self.message}{location}"
        )
