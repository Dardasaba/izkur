#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/client/__init__.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from .base import IsraeliLegislation, IsraeliDecision

__all__ = [
    "IsraeliLegislation",
    "IsraeliDecision",
]
