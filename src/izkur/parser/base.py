# -*- coding: utf-8 -*-
"""izkur/parser/base.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from dataclasses import dataclass
from abc import ABC

__all__ = ["ASTNode"]


@dataclass
class ASTNode(ABC):
    """Base class for all AST nodes."""

    pass


class ParseError(Exception):
    """Raised when parsing fails."""

    def __init__(self, message: str, position: int | None = None):
        self.message = message
        self.position = position
        super().__init__(
            f"Parse error at {position}: {message}" if position is not None else message
        )
