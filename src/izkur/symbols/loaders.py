# -*- coding: utf-8 -*-
"""izkur/symbols/loaders.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from typing import Union
from izkur.symbols.base import CourtSymbol, CollectionSymbol, LegislationSymbol
from izkur.symbols.symbol_table import SymbolTable

__all__ = ["load_default_symbols"]


def load_default_symbols() -> (
    SymbolTable[Union[CourtSymbol, CollectionSymbol, LegislationSymbol]]
):
    table: SymbolTable[Union[CourtSymbol, CollectionSymbol, LegislationSymbol]] = (
        SymbolTable()
    )

    # Courts
    table.register(
        CourtSymbol(
            name="בית המשפט העליון", abbreviation='בג"ץ', type="court", seat="ירושלים"
        )
    )
    table.register(
        CourtSymbol(name="בית הדין הרבני הגדול", abbreviation='פד"ר', type="court")
    )

    # Collections
    table.register(
        CollectionSymbol(
            name="פסקי דין עליונים",
            abbreviation='פ"ד',
            type="collection",
            publisher="לשכת עורכי הדין",
        )
    )

    # Legislation
    table.register(
        LegislationSymbol(
            name="פקודת הנזיקין",
            abbreviation="פק'",
            type="legislation",
            year_established=1944,
        )
    )

    return table
