# -*- coding: utf-8 -*-
"""izkur/errors/__init__.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from izkur.errors.base import ParseError
from izkur.errors.handler import ErrorHandler

__all__ = ["ParseError", "ErrorHandler"]
