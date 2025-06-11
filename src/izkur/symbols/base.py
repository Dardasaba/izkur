# -*- coding: utf-8 -*-
"""izkur/symbols/base.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from dataclasses import dataclass
from typing import Literal, Optional

__all__ = ["Symbol", "CourtSymbol", "LegislationSymbol", "CollectionSymbol"]


@dataclass(frozen=True)
class Symbol:
    name: str
    abbreviation: str
    type: Literal["court", "collection", "legislation", "generic"]


@dataclass(frozen=True)
class CourtSymbol(Symbol):
    seat: Optional[str] = None


@dataclass(frozen=True)
class LegislationSymbol(Symbol):
    year_established: Optional[int] = None
    hebrew_year: Optional[str] = None


@dataclass(frozen=True)
class CollectionSymbol(Symbol):
    publisher: Optional[str] = None
