#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/assets/__init__.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from .case_types_abbreviations import CASE_TYPES_ABBREVIATIONS
from .court_abbreviations import COURT_ABBREVIATIONS
from .court_seats import COURT_SEATS
from .decisions_collections import DECISIONS_COLLECTIONS
from .footnotes_abbreviations import FOOTNOTES_ABBREVIATIONS
from .internal_provisions import INTERNAL_PROVISIONS
from .legislation_collections import LEGISLATION_COLLECTIONS

__all__ = [
    "CASE_TYPES_ABBREVIATIONS",
    "COURT_ABBREVIATIONS",
    "COURT_SEATS",
    "DECISIONS_COLLECTIONS",
    "FOOTNOTES_ABBREVIATIONS",
    "INTERNAL_PROVISIONS",
    "LEGISLATION_COLLECTIONS",
]
