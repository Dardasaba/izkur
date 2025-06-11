# -*- coding: utf-8 -*-
"""izkur/errors/handler.py"""

__version__ = "0.2.0"
__date__ = "2025-06-11"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

__all__ = ["ErrorHandler"]

from izkur.errors.base import ParseError
from typing import List


class ErrorHandler:
    def __init__(self):
        self.errors: List[ParseError] = []

    def report(self, error: ParseError):
        self.errors.append(error)

    def has_errors(self, min_severity: str = "error") -> bool:
        severities = ["info", "warning", "error", "critical"]
        threshold_index = severities.index(min_severity)
        return any(severities.index(e.severity) >= threshold_index for e in self.errors)

    def raise_if_errors(self):
        if self.has_errors("error"):
            raise Exception("Parsing failed due to one or more errors.")

    def print_summary(self):
        for e in self.errors:
            print(e)
