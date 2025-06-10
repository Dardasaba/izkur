#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/__init__.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from .config import PROJECT_ROOT, BIN, LOGS
from .models import Abbreviation, CourtAbbreviation, DecisionsCollection
from .assets import (
    CASE_TYPES_ABBREVIATIONS,
    COURT_ABBREVIATIONS,
    COURT_SEATS,
    DECISIONS_COLLECTIONS,
    FOOTNOTES_ABBREVIATIONS,
    INTERNAL_PROVISIONS,
    LEGISLATION_COLLECTIONS,
)
from .helpers import (
    AsyncTyper,
    echo_info,
    echo_success,
    echo_warning,
    echo_error,
    echo_header,
    intervals_extract,
    intervals_to_str,
    determine_obj_using_hints,
    resolve_court,
    resolve_court_seat,
    resolve_court_type,
    resolve_decision_collection,
    get_obj_from_abbreviation,
)
from .client import IsraeliLegislation, IsraeliDecision

__all__ = [
    "PROJECT_ROOT",
    "BIN",
    "LOGS",
    "Abbreviation",
    "CourtAbbreviation",
    "DecisionsCollection",
    "CASE_TYPES_ABBREVIATIONS",
    "COURT_ABBREVIATIONS",
    "COURT_SEATS",
    "DECISIONS_COLLECTIONS",
    "FOOTNOTES_ABBREVIATIONS",
    "INTERNAL_PROVISIONS",
    "LEGISLATION_COLLECTIONS",
    "AsyncTyper",
    "echo_info",
    "echo_success",
    "echo_warning",
    "echo_error",
    "echo_header",
    "intervals_extract",
    "intervals_to_str",
    "determine_obj_using_hints",
    "resolve_court",
    "resolve_court_seat",
    "resolve_court_type",
    "resolve_decision_collection",
    "get_obj_from_abbreviation",
    "IsraeliLegislation",
    "IsraeliDecision",
]
