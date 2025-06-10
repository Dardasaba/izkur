#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""izkur/config/config.py"""

__version__ = "0.1.0"
__date__ = "2025-06-10"
__author__ = r"Dardasaba <almatsuy@gmail.com>"

from pathlib import Path
from configparser import ConfigParser

__all__ = [
    "PROJECT_ROOT",
    "BIN",
    "LOGS",
]

CONFIG_PATH = Path(__file__).parent / "config.ini"

parser = ConfigParser()
parser.read(CONFIG_PATH)

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_path_from_config(key: str, default_relative: str) -> Path:
    """Get path from config if defined, otherwise use project-root-relative default."""
    if parser.has_option("DEFAULT", key):
        return Path(parser.get("DEFAULT", key)).expanduser().resolve()
    return PROJECT_ROOT / default_relative


BIN = get_path_from_config("Bin", ".bin")
LOGS = get_path_from_config("Logs", "logs")
