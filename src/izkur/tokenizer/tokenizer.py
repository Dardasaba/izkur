# -*- coding: utf-8 -*-
"""izkur/tokenizer/tokenizer.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

import re
from enum import Enum, auto
from dataclasses import dataclass
from typing import Iterator

__all__ = ["TokenType", "Token", "tokenize"]


class TokenType(Enum):
    COURT = auto()
    YEAR = auto()
    NUMBER = auto()
    LEGISLATION_TITLE = auto()
    COMMA = auto()
    WHITESPACE = auto()
    EOF = auto()
    UNKNOWN = auto()


@dataclass
class Token:
    type: TokenType
    value: str
    position: int


# Token specification ordered by priority
TOKEN_REGEX = [
    (TokenType.WHITESPACE, r"\s+"),  # Ignore or skip
    (TokenType.COMMA, r","),  # Comma
    (TokenType.YEAR, r"\b(19|20)\d{2}\b"),  # Years 1900–2099
    (TokenType.NUMBER, r"\b\d+\b"),  # Case number, page number
    (TokenType.COURT, r"\bבג״ץ|\bע״פ|\bת״פ"),  # Hebrew court abbreviations
    (TokenType.LEGISLATION_TITLE, r"[^,\d]{2,}"),  # Catch-all for law titles (rough)
]

MASTER_REGEX = re.compile(
    "|".join(f"(?P<{tt.name}>{pattern})" for tt, pattern in TOKEN_REGEX)
)


def tokenize(text: str) -> Iterator[Token]:
    position = 0
    for match in MASTER_REGEX.finditer(text):
        kind = match.lastgroup
        value = match.group()
        if kind == "WHITESPACE":
            pass  # Skip whitespace tokens
        elif kind is not None:
            yield Token(TokenType[kind], value, match.start())
        else:
            yield Token(TokenType.UNKNOWN, value, match.start())
        position = match.end()
    yield Token(TokenType.EOF, "", position)
