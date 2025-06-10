#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/assets/footnotes_abbreviations.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from ..models import Abbreviation

__all__ = ["FOOTNOTES_ABBREVIATIONS"]

FOOTNOTES_ABBREVIATIONS: list[Abbreviation] = []

FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="הערת סיום",
        abbreviation='ה"ס',
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="הערות סיום",
        abbreviation='ה"ס',
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="הערת שוליים",
        abbreviation='ה"ש',
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="הערות שוליים",
        abbreviation='ה"ש',
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="סעיף",
        abbreviation="ס'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="סעיפים",
        abbreviation="ס'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="סימן",
        abbreviation="סי'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="סימנים",
        abbreviation="סי'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="עמוד",
        abbreviation="עמ'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="עמודים",
        abbreviation="עמ'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="פסקה",
        abbreviation="פס'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="פסקאות",
        abbreviation="פס'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="תוספת",
        abbreviation="תוס'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="תוספות",
        abbreviation="תוס'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="תקנה",
        abbreviation="תק'",
    )
)
FOOTNOTES_ABBREVIATIONS.append(
    Abbreviation(
        title="תקנות",
        abbreviation="תק'",
    )
)
