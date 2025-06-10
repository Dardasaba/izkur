#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/models/classes.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from dataclasses import dataclass

__all__ = ["Abbreviation", "CourtAbbreviation", "DecisionsCollection"]


@dataclass
class Abbreviation:
    title: str
    abbreviation: str = ""


@dataclass
class CourtAbbreviation(Abbreviation):
    indicate_seat: bool = True
    indicate_title: bool = True
    separator: str = "נ'"


@dataclass
class DecisionsCollection(Abbreviation):
    mandatory: bool = False
    description: str = ""
