# -*- coding: utf-8 -*-
"""izkur/symbols/symbol_table.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from collections import defaultdict
from typing import TypeVar, Generic, Optional, Literal, DefaultDict

from izkur.symbols.base import Symbol

__all__ = ["SymbolTable"]

T = TypeVar("T", bound=Symbol)


class SymbolTable(Generic[T]):
    def __init__(self):
        self._symbols_by_abbr: dict[str, T] = {}
        self._symbols_by_name: dict[str, T] = {}
        self._symbols_by_type: DefaultDict[
            Literal["court", "collection", "legislation", "generic"], dict[str, T]
        ] = defaultdict(dict)

    def register(self, symbol: T):
        self._symbols_by_abbr[symbol.abbreviation] = symbol
        self._symbols_by_name[symbol.name] = symbol
        self._symbols_by_type[symbol.type][symbol.abbreviation] = symbol

    def get_by_abbr(self, abbr: str) -> Optional[T]:
        return self._symbols_by_abbr.get(abbr)

    def get_by_name(self, name: str) -> Optional[T]:
        return self._symbols_by_name.get(name)

    def get_by_type(
        self, symbol_type: Literal["court", "collection", "legislation", "generic"]
    ) -> dict[str, T]:
        return self._symbols_by_type[symbol_type]

    def all(self) -> list[T]:
        return list(self._symbols_by_abbr.values())
