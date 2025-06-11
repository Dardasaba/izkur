# -*- coding: utf-8 -*-
"""izkur/parser/parser.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

__all__ = ["Parser"]

from typing import Union
from izkur.tokenizer.tokenizer import Token, TokenType
from izkur.errors.base import ParseError
from izkur.parser.nodes import IsraeliLegislationNode, IsraeliCaseNode
from izkur.symbols.symbol_table import SymbolTable
from izkur.symbols.base import CourtSymbol, CollectionSymbol, LegislationSymbol


class Parser:
    def __init__(
        self,
        tokens: list[Token],
        symbol_table: SymbolTable[
            Union[CourtSymbol, CollectionSymbol, LegislationSymbol]
        ],
    ):
        self.tokens = tokens
        self.pos = 0
        self.symbol_table = symbol_table

    def peek(self) -> Token | None:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def advance(self) -> Token:
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def match(self, expected_type: TokenType) -> Token:
        token = self.peek()
        if not token or token.type != expected_type:
            raise ParseError(
                message=f"Expected {expected_type}, got {token.type if token else 'EOF'}",
                stage="syntactic",
                severity="error",
                source_text=token.value if token else None,
                position=token.position if token else self.pos,
                hint="Check for a missing or misplaced token.",
            )
        return self.advance()

    def parse(self):
        # entry point: try each root rule
        if self.peek() and self.peek().type == TokenType.COURT:
            return self.parse_case()
        else:
            return self.parse_legislation()

    def parse_legislation(self) -> IsraeliLegislationNode:
        title = self.match(TokenType.LEGISLATION_TITLE).value
        year = self.match(TokenType.YEAR).value
        page = int(self.match(TokenType.NUMBER).value)
        return IsraeliLegislationNode(title=title, year=year, page=page)

    def parse_case(self) -> IsraeliCaseNode:
        court = self.match(TokenType.COURT).value
        year = self.match(TokenType.YEAR).value
        case_number = self.match(TokenType.NUMBER).value
        return IsraeliCaseNode(court=court, year=year, case_number=case_number)
