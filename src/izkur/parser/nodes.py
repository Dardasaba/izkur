# -*- coding: utf-8 -*-
"""izkur/parser/nodes.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from dataclasses import dataclass
from izkur.parser.base import ASTNode

__all__ = ["IsraeliLegislationNode", "IsraeliCaseNode"]


@dataclass
class IsraeliLegislationNode(ASTNode):
    title: str
    year: str
    page: int


@dataclass
class IsraeliCaseNode(ASTNode):
    court: str
    year: str
    case_number: str
